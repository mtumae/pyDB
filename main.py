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
    




def select(self, table_name, given_index):
        """
        Selects data from the specified table.

        Args:
            table_name (str): The name of the table to select from.
            conditions (dict, optional): The conditions to filter the data.
        Returns:
            data (str): The data from the specified table.
        """
        with open("./mockdata.csv", "r", newline='') as f:
            reader = csv.reader(f)
            starting_index = cache[table_name]['starting_index'] 
            ending_index = cache[table_name]['starting_index'] + cache[table_name]['columns']
            for index, row in enumerate(reader):
                if index == given_index:
                    print(row[starting_index:ending_index])
                    break
        return




# conditions {
    #"query": "m",
    #"table_name": "users",
#}
def query(self, conditions):
        """
        Queries data from the specified table based on conditions.

        Args:
            table_name (str): The name of the table to query.
            conditions (dict): The conditions to filter the data.

        Returns:
            data (str): The data from the specified table that meets the conditions.
        """
           
        with open("./mockdata.csv", "r", newline='') as f:
            start_time= time.perf_counter()
            reader = csv.reader(f)
            count = 0
            starting_index = cache[conditions['table_name']]['starting_index'] 
            ending_index = cache[conditions['table_name']]['starting_index'] + cache[conditions['table_name']]['columns']
            for row in reader:
                if conditions['query'] in row: 
                    print(f"Found {conditions['query']} in row: {count}: \n {row[starting_index:ending_index]} ")
                    break
                count +=1
            end_time = time.perf_counter()
        print(f"Took {float(end_time-start_time)}s")


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