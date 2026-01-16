import time
import csv
import json

cache = [] # load table metadata into memory
with open("./schema.json", "r") as sf:
    metadata = json.load(sf)
    cache = metadata
        



def create_table(self, table_name, columns):
        """
        Creates a new table in the schema file.

        Args:
            table_name (str):The name of the table to insert into.
            columns(list): The columns for the table.

        Returns:
            None
        """
        return

def insert(table_name, values):
        """
        Inserts a new row into the specified table.

        Args:
            table_name (str): The name of the table to insert into.
            values (list): The values to insert into the table.

        Returns:
            None
        """
        return
    


def select(self, table_name):
        """
        Selects data from the specified table.

        Args:
            table_name (str): The name of the table to select from.

        Returns:
            data (str): The data from the specified table.
        """
        return


def update(self, table_name, values):
        """
        Updates data in the specified table.

        Args:
            table_name (str): The name of the table to update.
            values (list): The new values to update in the table.

        Returns:
            None
        """
        return



def get_table(table_name, cache):
        """
        Retrieves the data from the given table name.

        Args:
            table_name (str): The name of the table to retrieve.

        """
        start_time= time.perf_counter()
        with open("./mockdata.csv", "r", newline='') as f:
            csv_reader = csv.reader(f)
            starting_index = cache[table_name]['starting_index']+1 
            ending_index = cache[table_name]['starting_index'] + cache[table_name]['columns']+1
            for row in csv_reader:
                print(row[starting_index:ending_index]) 
            end_time = time.perf_counter()