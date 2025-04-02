# main.py
# Student Name: Dylan Sams, Andrew Rozsits, Omar Alkhawaga
# email:  samsds@mail.uc.edu, rozsitaj@mail.uc.edu, alkhawoe@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/2/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  {required}

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant::
import pyodbc
from databaseManagementPackage.databaseManagement import *
from ManufacturerPackage.manufacturer import *
from BrandPackage.brand import *


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

    print(f"Selected Product:\n- Description: {description}\n- ProductID: {product_id}\n- ManufacturerID: {manufacturer_id}\n- BrandID: {brand_id}")

    manufacturer_name = manufacturer_service.get_manufacturer_name(manufacturer_id)
    print(f"Manufacturer Name: {manufacturer_name}")

    