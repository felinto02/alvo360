import mysql.connector
from mysql.connector import Error
import base64

def buscar_dados_cliente(cliente_id):
    try:
        # Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host='localhost',
            database='operacao',
            user='root',
            password=''
        )

        if conexao.is_connected():
            cursor = conexao.cursor(dictionary=True)

            # Consultar todas as informações do cliente
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

            # Converte foto_casa para Base64 se existir
            if dados_endereco and dados_endereco['foto_casa']:
                dados_endereco['foto_casa'] = base64.b64encode(dados_endereco['foto_casa']).decode('utf-8')

            # Buscar fotos
            query_fotos = """SELECT * FROM fotos WHERE cliente_id = %s"""
            cursor.execute(query_fotos, (cliente_id,))
            dados_fotos = cursor.fetchone()

            # Verifique se existem fotos e converta para Base64
            if dados_fotos:
                if 'foto1' in dados_fotos and dados_fotos['foto1']:
                    dados_fotos['foto1'] = base64.b64encode(dados_fotos['foto1']).decode('utf-8')
                if 'foto2' in dados_fotos and dados_fotos['foto2']:
                    dados_fotos['foto2'] = base64.b64encode(dados_fotos['foto2']).decode('utf-8')

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
        if 'conexao' in locals() and conexao.is_connected():
            cursor.close()
            conexao.close()
