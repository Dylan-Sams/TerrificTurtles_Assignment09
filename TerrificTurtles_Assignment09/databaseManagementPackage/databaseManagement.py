# databaseManagement.py
# Student Name: Dylan Sams, Andrew Rozsits, Omar Alkhawaga
# email:  samsds@mail.uc.edu, rozsitaj@mail.uc.edu, alkhawoe@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/2/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant:

import pyodbc

class databaseManagement(object):
    def connect_to_database(self):
        """
        Connect to our SQL Server instance
        @return the connection object or None if failure
        """
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                                  'Database=GroceryStoreSimulator;'
                                  'uid=IS4010Login;'
                                  'pwd=P@ssword2;')
            return conn
        except:
            return None
    def submit_sql_to_server(self,conn, sql_statement):
        """
        submit a SQL statement to our server
        @param conn connection object: The connection object
        @param sql_statement String: The SQL to submit
        @return The pyodbc cursor object that contains the query results
        """
        cursor = conn.cursor()
        cursor.execute(sql_statement)
        return cursor