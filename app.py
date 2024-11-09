from flask import Flask, render_template, request, redirect, url_for, make_response
from buscar_dados import buscar_dados_cliente

app = Flask(__name__)

# Rota para a página inicial com o cliente_id
@app.route('/<int:cliente_id>')
def pagina_inicial(cliente_id):
    # Busca os dados do cliente
    dados_cliente = buscar_dados_cliente(cliente_id)

    if dados_cliente:
        # Define o cookie com o cliente_id
        response = make_response(render_template('home.html', dados=dados_cliente, is_home=True))
        response.set_cookie('cliente_id', str(cliente_id), max_age=60*60*24)  # Expira em 1 dia
        return response
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500

# Rota para a página inicial (home) sem cliente_id
@app.route('/')
def home_root():
    # Tenta obter o cliente_id do cookie
    cliente_id = request.cookies.get('cliente_id')
    if cliente_id:
        # Redireciona para a página inicial com o cliente_id do cookie
        return redirect(url_for('pagina_inicial', cliente_id=int(cliente_id)))
    else:
        # Se o cliente_id não estiver no cookie, retorna um erro
        return "Erro: cliente_id não encontrado", 400


# Rota para outras páginas com cliente_id e nome de página
@app.route('/<pagina>')
@app.route('/<pagina>/<int:cliente_id>')
def exibir_dados(pagina, cliente_id=None):
    # Se o cliente_id não for fornecido na URL, tenta obter do cookie
    if cliente_id is None:
        cliente_id = request.cookies.get('cliente_id')
        if not cliente_id:
            return "Erro: cliente_id não encontrado", 400  # Erro se cliente_id não está disponível
        cliente_id = int(cliente_id)  # Converte de string para int

    # Busca os dados do cliente
    dados_cliente = buscar_dados_cliente(cliente_id)

    if dados_cliente:
        # Renderizar diferentes templates baseados no valor de 'pagina'
        if pagina == 'informacao':
            return render_template('informacao.html', dados=dados_cliente)
        elif pagina == 'fotos':
            return render_template('fotos.html', dados=dados_cliente)
        elif pagina == 'endereco':
            return render_template('endereco.html', dados=dados_cliente)
        elif pagina == 'qualificacao':
            return render_template('qualificacao.html', dados=dados_cliente)
        elif pagina == 'mapa':
            return render_template('mapa.html', dados=dados_cliente)
        else:
            return "Página não encontrada", 404
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500

# Função principal para rodar a aplicação
if __name__ == "__main__":
    app.run(debug=True)
