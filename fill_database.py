import pandas as pd
import sqlite3
from pandas.io import sql
import subprocess

# In and output file paths
in_csv = './sample-data/bills-with-urls.csv'
out_sqlite = './sample-data/legislation.db'

table_name = 'tBills' # name for the SQLite database table
chunksize = 100000 # number of lines to process at each iteration

# columns that should be read from the CSV file
columns = ['bill_id','bill_number','title','description','state',
           'session','filename','status','status_date','url','error','content']


# Get number of lines in the CSV file
nlines = subprocess.check_output(['wc', '-l', in_csv])
nlines = int(nlines.split()[0]) 

# connect to database
conn = sqlite3.connect(out_sqlite)

# Iteratively read CSV and dump lines into the SQLite table
for i in range(0, nlines, chunksize):  # change 0 -> 1 if your csv file contains a column header
    
    df = pd.read_csv(in_csv,  
            header=None,  # no header, define column header manually later
            nrows=chunksize, # number of rows to read at each iteration
            skiprows=i)   # skip rows that were already read
    
    # columns to read        
    df.columns = columns

    sql.to_sql(df, 
                name=table_name, 
                con=conn, 
#                index=False, # don't use CSV file index
#                index_label='molecule_id', # use a unique column from DataFrame as index
                if_exists='append') 
conn.close()    