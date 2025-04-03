# manufacturer.py
# Student Name: Dylan Sams, Andrew Rozsits, Omar Alkhawaga
# email:  samsds@mail.uc.edu, rozsitaj@mail.uc.edu, alkhawoe@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:   4/3/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment is working  in teams to create a project that accesses our SQL Server and extracts some data from the Grocery Store Simulator database, and produces some results.

# Brief Description of what this module does. This module instantiates the class ManufacturerService and uses the module get_manufacturer_name to use the manufacturer_id to get the manufacturer name
# Citations: Connect SQL Server to Python: https://medium.com/@noueruzzaman/how-to-connect-sql-server-with-python-in-visual-studio-code-2496593e9733

# Anything else that's relevant:


class ManufacturerService:
    def __init__(self, connection):
        self.connection = connection

    def get_manufacturer_name(self, manufacturer_id):
        """
        Fetches the manufacturer name from the tManufacturer table using a given ID.

        Parameters:manufacturer_id (int): The ID of the manufacturer.

        Returns:str: The name of the manufacturer if found, otherwise "Unknown".
        """
        cursor = self.connection.cursor()
        query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result.Manufacturer if result else "Unknown"
    
    