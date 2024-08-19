from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv() # load all the envirnment variables

## Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Model provide sql Query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content([f"{prompt}\n{question}"])
    return response.text

## Function to retrieve query from the sql database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    print(f"Executing SQL: {sql}")
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    print(f"Rows fetched: {rows}")
    for row in rows:
        print(row)
    return rows

## Define Your Prompt

prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS \n\nFor example, \nExample 1 - How many entries of records are present?
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?
    The SQL command will be something like this: SELECT * FROM STUDENT 
    where CLASS="Data Science";
    also the sql code should not have ```in beginning or end and sql world in the output
"""
]


#streamlit App

st.set_page_config(page_title='I can Retrieve Any SQL query')
st.header("Lakshaya Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

# if submit is clicked

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.write(row)
