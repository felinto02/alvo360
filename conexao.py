import os
import mysql.connector
from mysql.connector import Error

def create_connection():
    """Create a database connection."""
    db_host = os.getenv('DB_HOST')
    db_database = os.getenv('DB_DATABASE')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    try:
        connection = mysql.connector.connect(
            host=db_host,
            database=db_database,
            user=db_user,
            password=db_password
        )
        if connection.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso!")
            return connection
    except Error as err:
        print(f"Erro ao conectar ao MySQL: {err}")
        return None

def close_connection(connection):
    """Close the database connection."""
    if connection and connection.is_connected():
        connection.close()
        print("Conexão com o banco de dados encerrada.")
