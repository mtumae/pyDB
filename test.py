import json
import csv
import time

cache = [] # will contain table meta data

with open("./schema.json", "r") as sf:
    metadata = json.load(sf)
    cache = metadata
        


table_name = "users"
# this should get the table
start_time= time.perf_counter()
with open("./mockdata.csv", "r", newline='') as f:
    csv_reader = csv.reader(f)
    starting_index = cache[table_name]['starting_index']+1 
    ending_index = cache[table_name]['starting_index'] + cache[table_name]['columns']+1
    for row in csv_reader:
        # using schema get where to start and end for the given table name
        print(row[starting_index:ending_index]) # replace users with table name
    end_time = time.perf_counter()


    
    
   
        
        

    




          
        
  
    

