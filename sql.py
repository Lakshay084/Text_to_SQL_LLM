import sqlite3

##conect to sqlite
connection=sqlite3.connect("student.db")

## create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

## create the table
table_info="""
CREATE TABLE STUDENT (
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
);
"""

cursor.execute(table_info)

## Insert Some more records

cursor.execute(''' Insert Into STUDENT values('Krish','Data Science', 'A', 90)''')
cursor.execute(''' Insert Into STUDENT values('Sudhanshu','Data Science', 'B', 100)''')
cursor.execute(''' Insert Into STUDENT values('Darius','Data Science', 'A', 86)''')
cursor.execute(''' Insert Into STUDENT values('Vikash','DEVOPS', 'A', 50)''')
cursor.execute(''' Insert Into STUDENT values('Dipesh','DEVOPS', 'A', 35)''')
    
##except sqlite3.Error as e:
   ### print(f"An error occurred: {e}")    

## Display all the records

print("The inserted record are")

#try:
#    data = cursor.execute("SELECT * FROM STUDENTS")
#   for row in data:
#        print(row)
        
#except sqlite3.Error as e:
 #   print(f"An error occurred while fetching data: {e}")        

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)
    
## Close the connection

connection.commit()
connection.close()
