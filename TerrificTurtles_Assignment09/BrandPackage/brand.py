# brand.py
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


import random

class ProductService:
    def __init__(self, connection):
        self.connection = connection

    def fetch_all_products(self):
        """
        Retrieves all product records from the tProduct table.
        Returns: list: A list of product rows (pyodbc.Row objects).
        """

        cursor = self.connection.cursor()
        query = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def get_random_product(self, product_list):
        """
        Randomly selects one product from a given list.

        Parameters:product_list (list): List of product rows.

        Returns:pyodbc.Row: A randomly selected product row.
        """
        return random.choice(product_list)