# main.py
# Student Name: Dylan Sams, Andrew Rozsits, Omar Alkhawaga
# email:  samsds@mail.uc.edu, rozsitaj@mail.uc.edu, alkhawoe@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment is working  in teams to create a project that accesses our SQL Server and extracts some data from the Grocery Store Simulator database, and produces some results.

# Brief Description of what this module does. This module creates an instance of the all classes to generate and print their output to the console
# Citations: 

# Anything else that's relevant::
import pyodbc
from databaseManagementPackage.databaseManagement import *
from ManufacturerPackage.manufacturer import *
from BrandPackage.brand import *
from sumOfItemsSoldPackage.sumOfItemsSold import *

if __name__ == "__main__":
    dbm = databaseManagement()
    conn = dbm.connect_to_database()
    
    product_service = ProductService(conn)
    manufacturer_service = ManufacturerService(conn)

    products = product_service.fetch_all_products()
    selected = product_service.get_random_product(products)
    product_id = selected.ProductID
    description = selected.Description
    manufacturer_id = selected.ManufacturerID
    brand_id = selected.BrandID
    
    items_sold = get_items_sold(product_id)
    
    manufacturer_name = manufacturer_service.get_manufacturer_name(manufacturer_id)
    
    brand_name = product_service.get_brand_name(brand_id)
    

    print(f"The product {brand_name} {description} manufactured by {manufacturer_name}, has sold {items_sold} units.")