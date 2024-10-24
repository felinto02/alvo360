import mysql.connector
from mysql.connector import Error
from datetime import datetime


def buscar_dados_cliente(cliente_id):
    try:
        # Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host='localhost',  # Ajustar conforme o host do banco de dados
            database='operacao',  # Nome do banco de dados
            user='root',  # Nome de usuário do banco de dados
            password=''  # Senha do banco de dados
        )

        if conexao.is_connected():
            cursor = conexao.cursor(dictionary=True)

            # Consultar todas as informações do cliente, com a data formatada
            query_cliente = """
                SELECT cliente_id, nome, nome_mae, nome_pai, 
                       DATE_FORMAT(data_nasc, '%d/%m/%Y') AS data_nasc,
                       nat, nat_uf, cpf, rg, telefone, telefone_secundario, observacao
                FROM alvo WHERE cliente_id = %s
            """
            cursor.execute(query_cliente, (cliente_id,))
            dados_cliente = cursor.fetchone()

            query_endereco = """SELECT * FROM endereco WHERE cliente_id = %s"""
            cursor.execute(query_endereco, (cliente_id,))
            dados_endereco = cursor.fetchone()

            query_fotos = """SELECT * FROM fotos WHERE cliente_id = %s"""
            cursor.execute(query_fotos, (cliente_id,))
            dados_fotos = cursor.fetchone()

            query_informacoes = """SELECT * FROM informacoes WHERE cliente_id = %s"""
            cursor.execute(query_informacoes, (cliente_id,))
            dados_informacoes = cursor.fetchone()

            # Juntar todas as informações em um único dicionário
            dados_completos = {
                'cliente': dados_cliente,
                'endereco': dados_endereco,
                'fotos': dados_fotos,
                'informacoes': dados_informacoes
            }

            return dados_completos

    except Error as e:
        print(f"Erro ao buscar dados do cliente: {e}")
        return None
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
