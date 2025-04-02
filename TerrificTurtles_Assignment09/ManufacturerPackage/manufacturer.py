# manufacturer.py
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