
# Python Assignment

 Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.Python supports modules and packages, which encourages program modularity and code reuse.

# Context

In this assignment I am going create json file.Connected with mysql. Then create database.Read each csv file into pandas dataframe.Load pandas dataframe to mysql.

# Libaries
In this Assignment I am import suitable libaries which is useful to execute the program which are :

1) sys library : The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment.

2) os library : The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory.

3) json library : The JSON module is mainly used to convert the python dictionary above into a JSON string that can be written into a file.

4) argparse library : The argparse module in Python helps create a program in a command-line-environment in a way that appears not only easy to code but also improves interaction.

5) pandas library : pandas is a software library written for the Python programming language for data manipulation and analysis.

6) mysql connector : MySQL Connector/Python enables Python programs to access MySQL databases.


# Create utility

File_upload.py : utility is executed with necessary arguments it will
take a directory as an argument, and read all files from the directory, and
upload them to the corresponding MySQL table specified in config.

# Arguments
1) --source_dir : Source directory from which we need to read all files to
upload to MySQL

2) --mysql_details : Path of a JSON file which contains all details of MySQL
to which to connect to. 

3) --destination_table : Name of table to upload data to.

# Functions 

* json.load() : The json.loads() method allows us to convert a JSON string into an equivalent python object (dictionary).

* connect() : The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.

* cursor() : Allows Python code to execute PostgreSQL command in a database session. Cursors are created by the connection.

* iterrows() : It is used to iterate over a pandas Data frame rows in the form of (index, series) pair.

* cursor.execute() : This method executes the given database operation (query or command).

* argparse.ArgumentParser() : The argparse module makes it easy to write user-friendly command-line interfaces. It parses the defined arguments from the sys.

* add_argument() : It is used to add new parameter.

* tuple()  : Tuples are used for grouping data. Once Python has created a tuple in memory, it cannot be changed.

# License

[MIT](https://choosealicense.com/licenses/mit/)

This readme.md file is made in readme.so
