# brand.py
# Student Name: Dylan Sams, Andrew Rozsits, Omar Alkhawaga
# email:  samsds@mail.uc.edu, rozsitaj@mail.uc.edu, alkhawoe@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/2/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment is working  in teams to create a project that accesses our SQL Server and extracts some data from the Grocery Store Simulator database, and produces some results.
# Brief Description of what this module does. This module takes a brandID and wants to looks up the brand name
# Citations: 


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

    def __init__(self, connection):
        self.connection = connection

    def get_brand_name(self, brand_id):
        """
        Fetches the brand name from the tbrand table using a given ID.

        Parameters:brand_id (int): The ID of the brand.

        Returns:str: The name of the brand if found, otherwise "Unknown".
        """
        cursor = self.connection.cursor()
        query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result.Manufacturer if result else "Unknown"
    