import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def criar_conexao():
    """Cria uma conexão com o banco de dados MySQL usando variáveis de ambiente."""
    try:
        conexao = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_DATABASE'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida ao banco de dados.")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
