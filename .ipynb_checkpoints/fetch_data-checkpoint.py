from legiscan import LegiScan
import legiscan

import os
import pandas as pd
import swifter
import zipfile
import base64
import io
import glob
import time
import json
import requests
import mimetypes
import tqdm 

class FetchData: 
    
    PATH_OUTPUT = './sample-data-2/'
    
    def __init__(self
                 ): 
        self.api_key = os.environ.get('LEGISCAN_API_KEY')
        self.legis = LegiScan(self.api_key)
        self.__test_dataset__()
        self.find_json()
        self.process_json()
        self.create_dataframe()
       # self.df_to_csv()
        
        
    def check_directories(self): 
        if not os.path.exists(self.PATH_OUTPUT): 
            os.mkdir(self.PATH_OUTPUT)
        return
    
        
    def __test_dataset__(self): 
        self.__datasets = self.legis.get_dataset_list()
        self.__dataset = self.legis.get_dataset(self.__datasets[20]['session_id'], self.__datasets[20]['access_key'])
        return 
        
    def get_test_dataset(self): 
        return self.__dataset.copy()
    
    def decode_test_dataset(self): 
        # we need to decode the datasets into a normal file, using Python's zipfile module here
        dataset = self.__test_dataset__()
        __z_bytes__ = base64.b64decode(dataset['zip'])

        # create an in-memory stream for bytes data (io.BytesIO()) from decoded base64,
        #     then create a zipfile object using the zipfile module to store the bytes
        __z__ = zipfile.ZipFile(io.BytesIO(__z_bytes__))

        # extract all files in the zip file
        __z__.extractall(PATH_OUTPUT)
        return
        
    def find_json(self): 
        filenames = glob.glob("bill_data/*/*/bill/*.json")
        return filenames
    
    def get_json_filenames(self): 
        return self.find_json()
        
    def process_json(self):
        for filename in self.find_json(): 
            with open(filename) as file:
                bill_data = {}
                # We need to do a little string replacing so the 
                json_str = file.read().replace('"0000-00-00"', 'null')
                content = json.loads(json_str)['bill']

                bill_data['bill_id'] = content['bill_id']
                bill_data['code'] = os.path.splitext(os.path.basename(filename))[0]
                bill_data['bill_number'] = content['bill_number']
                bill_data['title'] = content['title']
                bill_data['description'] = content['description']
                bill_data['state'] = content['state']
                bill_data['session'] = content['session']['session_name']
                bill_data['filename'] = filename
                bill_data['status'] = content['status']
                bill_data['status_date'] = content['status_date']

                try:
                    bill_data['url'] = content['texts'][-1]['state_link']
                except:
                    pass
            return pd.Series(bill_data)
        
        def create_dataframe(self): 
            filenames = self.get_json()
            
            df = pd.Series(filenames).swifter.apply(self.process_json)
            return df
        
        def get_dataframe(self): 
            return self.create_dataframe
        
        def df_to_csv(self): 
            df.to_csv('PATH_OUTPUT' + '/bills-with-urls.csv', index=False)
            return 