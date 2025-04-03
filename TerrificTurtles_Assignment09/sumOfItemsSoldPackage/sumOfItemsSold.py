# sumOfItemsSold.py
# Student Name: Dylan Sams, Andrew Rozsits, Omar Alkhawaga
# email:  samsds@mail.uc.edu, rozsitaj@mail.uc.edu, alkhawoe@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment is working  in teams to create a project that accesses our SQL Server and extracts some data from the Grocery Store Simulator database, and produces some results.
# Brief Description of what this module does. This module takes a productID and sees how many of that product have been sold
# Citations: https://stackoverflow.com/questions/75348376/executing-a-sql-query-using-python
# Anything else that's relevant:N/A


from databaseManagementPackage.databaseManagement import databaseManagement 

def get_items_sold(product_id):
    """
    Fetches the number of items sold for the given product
    """
    db = databaseManagement()  
    conn = db.connect_to_database()  


    cursor = conn.cursor()
    query = f"""
        SELECT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
        FROM dbo.tTransactionDetail
        INNER JOIN dbo.tTransaction 
        ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
        WHERE dbo.tTransaction.TransactionTypeID = 1 
        AND dbo.tTransactionDetail.ProductID = {product_id}
    """

    cursor.execute(query)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result[0] if result and result[0] is not None else 0