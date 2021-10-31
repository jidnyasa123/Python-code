import sys
import os
import json
import argparse
import pandas as pd
import mysql.connector as c


def upload_file(source_dir,mysql_details,destination_table):
    dirs = os.listdir(source_dir)

    for file in dirs:
    

        emp = pd.read_csv(os.path.join(source_dir,file))
        print(emp)

        with open(mysql_details) as data_file:
            data1 = json.load(data_file)[0]
            mysql_ip = data1["mysql_ip"]
            port = data1["port"]
            username = data1["username"]
            password = data1["password"]
            database = data1["database"]
            print(f'{mysql_ip}-{port}-{username}-{password}')

            #establishing the connection
            conn=c.connect(host=mysql_ip,user=username,passwd=password,database=database)
            if conn.is_connected():
                #Creating a cursor object using the cursor() method
                cursor = conn.cursor()

                print("Successfully Connected....")
                for i,row in emp.iterrows():                   
                    #here %S means string values 
                    sql = "INSERT INTO emp (FIRST_NAME,LAST_NAME,SALARY) VALUES (%s,%s,%s)"                       

                    cursor.execute(sql, tuple(row))
                    print("Record inserted")
                    # the connection is not auto committed by default, so we must commit to save our changes
                    conn.commit()


            else:
                print("Some Connectivity Isuue...")


def main():
    # Create the parser
    my_parser = argparse.ArgumentParser()  

    # Add the arguments
    my_parser.add_argument('--source-dir', help='a first argument')

    my_parser.add_argument('--mysql-details',help='a second argument')

    my_parser.add_argument('--destination-table', help='a second argument')

    # Execute the parse_args() method
    args = my_parser.parse_args()
    
    upload_file(args.source_dir, args.mysql_details, args.destination_table)

if __name__ == "__main__":
    main()