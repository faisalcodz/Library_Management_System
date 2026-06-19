import mysql.connector
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ToJo10tojo",
        database="library_management_project"
    )