# pyDb

# Layers
Query planner - decides how to execute queries
Storage engine - decides how to read and write data to disk
Execution engine - executes queries using the storage engine


# Data types (column data types)
string
integer
float
boolean


I will use a file-based storage system with 
- a schema.json files to hold table metadata (I will change this to a python dictionary soon)
- a data.csv file to hold the actual data
