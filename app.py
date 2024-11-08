from flask import Flask, render_template, request
from buscar_dados import buscar_dados_cliente

app = Flask(__name__)

# Rota para a página inicial com o cliente_id
@app.route('/<int:cliente_id>')
def pagina_inicial(cliente_id):
    # Busca os dados do cliente
    dados_cliente = buscar_dados_cliente(cliente_id)

    if dados_cliente:
        # Página inicial, renderizando index.html ou qualquer outra página principal
        return render_template('index.html', dados=dados_cliente)  # Você pode personalizar a página que deseja exibir
    else:
        return f"Erro ao buscar os dados do cliente com ID {cliente_id}", 500

# Rota para capturar qualquer página com cliente_id e nome de página
@app.route('/<pagina>/<int:cliente_id>')
def exibir_dados(pagina, cliente_id):
    # Busca os dados do cliente
    dados_cliente = buscar_dados_cliente(cliente_id)

    if dados_cliente:
        # Verifica qual página deve ser renderizada
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
