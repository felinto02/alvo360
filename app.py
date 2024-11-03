from flask import Flask, render_template, send_from_directory, redirect, url_for
from buscar_dados import buscar_dados_cliente
from dotenv import load_dotenv
import os

load_dotenv()



app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

@app.route('/')
def index():
    cliente_id = 1  # Aqui, você deve ajustar o ID do cliente que deseja buscar
    dados = buscar_dados_cliente(cliente_id)  # Busca os dados do cliente
    

    
    # Verifique se os dados foram encontrados
    if dados:
        return render_template('index.html', dados=dados)  # Passa os dados para o template
    else:
        return "Cliente não encontrado", 404


@app.route('/fotos/<int:cliente_id>')
def fotos(cliente_id):
    # Buscar os dados do cliente no banco de dados
    dados_cliente = buscar_dados_cliente(cliente_id)

    # Renderizar a página qualificacao.html com os dados do cliente
    if dados_cliente:
        return render_template('fotos.html', dados=dados_cliente)
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500

@app.route('/fotos')
def fotos_home():
    return redirect(url_for('fotos', cliente_id=1))  # Altere 1 para o ID padrão desejado


@app.route('/endereco/<int:cliente_id>')
def endereco(cliente_id):
    # Buscar os dados do cliente no banco de dados
    dados_cliente = buscar_dados_cliente(cliente_id)


    # Renderizar a página endereco.html com os dados do cliente
    if dados_cliente:
        return render_template('endereco.html', dados=dados_cliente)
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500


@app.route('/endereco')
def rendrereco_home():
    return redirect(url_for('endereco', cliente_id=1))  # Altere 1 para o ID padrão desejado



@app.route('/qualificacao/<int:cliente_id>')
def qualificacao(cliente_id):
    # Buscar os dados do cliente no banco de dados
    dados_cliente = buscar_dados_cliente(cliente_id)

    # Renderizar a página qualificacao.html com os dados do cliente
    if dados_cliente:
        return render_template('qualificacao.html', dados=dados_cliente)
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500

@app.route('/qualificacao')
def qualificacao_home():
    return redirect(url_for('qualificacao', cliente_id=1))  # Altere 1 para o ID padrão desejado



@app.route('/mapa/<int:cliente_id>')
def mapa(cliente_id):
    # Buscar os dados do cliente no banco de dados
    dados_cliente = buscar_dados_cliente(cliente_id)

    # Renderizar a página mapa.html com os dados do cliente
    if dados_cliente:
        return render_template('mapa.html', dados=dados_cliente)
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500

@app.route('/mapa')
def mapa_home():
    return redirect(url_for('mapa', cliente_id=1))  # Altere 1 para o ID padrão desejado



@app.route('/informacao/<int:cliente_id>')
def informacao(cliente_id):
    # Buscar os dados do cliente no banco de dados
    dados_cliente = buscar_dados_cliente(cliente_id)

    # Renderizar a página informacao.html com os dados do cliente
    if dados_cliente:
        return render_template('informacao.html', dados=dados_cliente)
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500

@app.route('/informacao')
def informacao_home():
    return redirect(url_for('informacao', cliente_id=1))  # Altere 1 para o ID padrão desejado

@app.route('/imagens/<path:filename>')
def serve_image(filename):
    return send_from_directory('imagens', filename)


@app.route('/cliente/<int:cliente_id>')
def exibir_cliente(cliente_id):
    # Buscar os dados do cliente
    dados = buscar_dados_cliente(cliente_id)

    if dados:
        return render_template('cliente.html', dados=dados)
    else:
        return "Erro ao buscar os dados do cliente", 500


if __name__ == '__main__':
    app.run(debug=True)  # Modo de debug ativado
