import streamlit as st
import pandas as pd
import mysql.connector
import retail_orders_functions as rof
from streamlit_option_menu import option_menu

#SQL server connection
def get_sql_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "test",
        database = "retail_orders",
        )
    return connection

#Change sidebar,main page background color
st.markdown(
    """ 
    <style>
    section[data-testid="stSidebar"]{
    background-color:#A9A9A9; ; 
    }
    
    .main {
    background-color:#D3D3D3; 
    }

    header[data-testid="stHeader"]{
    background-color:#D3D3D3;
    }
    
    h1{
    color : #FF4500
    }
   </style>

    """, unsafe_allow_html=True)


#To execute SQL query
def fetch_data(query):
    conn = get_sql_connection()
    if conn:
        mycursor = conn.cursor(dictionary=True)
        mycursor.execute(query)
        data = mycursor.fetchall()
        conn.close()
        return pd.DataFrame(data)

#Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options = ["About Project","Mentor Insights","Additional Insights"],
        icons = ["info-circle","info-circle","info-circle"],
        menu_icon = "house",
        default_index=0    
    )
if selected == "About Project":
    st.balloons()
    st.title("Retail Order Data Analysis")
    st.markdown(""" 
    #### Objective:
    To analyze and optimize sales performance by identifying key trends, top-performing products,and growth opportunities using a dataset of sales transactions
    #### Project Mentor : Gomathi
    #### Skills take away from this project : 
    Kaggle Api, Python, SQL, Streamlit   
    """)

elif selected == "Mentor Insights":
    st.write("#### Mentor Insights")
    #SelectBox to select the question
    optionInput = st.selectbox('Select the Question',[rof.qn_one,rof.qn_two,rof.qn_three,
    rof.qn_four,rof.qn_five,rof.qn_six,rof.qn_seven,rof.qn_eight,rof.qn_nine,rof.qn_ten])
    query = rof.generate_query(optionInput)
    result = fetch_data(query)
    st.dataframe(result)

elif selected == "Additional Insights":
    st.write("#### Additional Insights")
    #SelectBox to select the question
    optionInput = st.selectbox('Select the Question',[rof.qn_eleven,rof.qn_twelve,rof.qn_thirteen,
    rof.qn_fourteen,rof.qn_fifteen,rof.qn_sixteen,rof.qn_seventeen,rof.qn_eighteen,rof.qn_nineteen,rof.qn_twenty])
    query = rof.generate_query(optionInput)
    result = fetch_data(query)
    st.dataframe(result) 



