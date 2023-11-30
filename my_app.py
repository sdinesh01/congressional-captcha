import create_database
from create_database import MyDB
from bill_text import Bill
import bill_text
import pandas as pd
import streamlit as st
import io

class MyApp:
    def __init__(self):
        self.db = MyDB(bills_drop=True, any_drop=True, add_data=True, table_type='bills', input_lim=200, chunk_size=500)
        self.build_page()
        return

    # main build_page method
    def build_page(self):
        st.write('# Legislation tracker')
        
        st.sidebar.header('State and session selection')
        st.write("I'm just trying to get something to show up here!!!")
        self.select_state()
        self.select_session()
        self.get_bills()
        self.get_bill_text()
        
#         st.write('\n---\n## Executive Dashboard')
#         self.build_sales_plot()

#         st.write('\n---\n### Customer Tracker')
#         self.build_customer_tracker()
        
        self.streamlit_defaults()
        return
    
    def select_state(self): 
        self.states = self.db.run_query('SELECT DISTINCT state FROM tBills;')['state'].tolist()
        self.state_choice = st.sidebar.selectbox('Select a state:', self.states)
        return
    
    def select_session(self): 
        self.sessions = self.db.run_query('SELECT DISTINCT session FROM tBills WHERE state = (?);', (self.state_choice,))['session'].tolist()
        self.session_choice = st.sidebar.selectbox('Select a session:', self.sessions)
        return
    
    def get_bills(self): 
        self.query = """ SELECT * 
                FROM tBills
                WHERE state = (?) AND session = (?)
                ;"""
        results = self.db.run_query(sql=self.query, params=(self.state_choice, self.session_choice))
        return st.dataframe(results)
    
    def retreive_bill_text(self):
        self.db.connect()
        still_unprocessed = pd.read_sql("""SELECT bill_id FROM tBills
                                           WHERE processed_at IS NULL AND state = (?) AND session = (?);""", con=self.db.conn, params=(self.state_choice, self.session_choice))
        id_nums = still_unprocessed['bill_id'].tolist()
        for i in id_nums: 
            bill = Bill.get(self.db.conn, i)
            bill.update_content()
        self.db.close()
        return 
    
    def get_bill_text(self):
        self.retreive_bill_text()
        self.query = """ SELECT content 
                        FROM tBills
                        WHERE state = (?) AND session = (?)
                        ;"""
        results = self.db.run_query(sql=self.query, params=(self.state_choice, self.session_choice))
        return st.text(results)
    

    def streamlit_defaults(self):
        '''
        Remove some auto-generated stuff by streamlit
        '''
        hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
        return