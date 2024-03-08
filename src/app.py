from flask import Flask, render_template, request, redirect, url_for, session, flash
from tinydb import TinyDB, Query

app = Flask(__name__)

dbCaminhos = TinyDB('caminhos.json', indent=4)

# Configuração para recarregar os templates (Páginas HTML) automaticamente
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/novo", methods=['GET', 'POST'])
def novo():
    if request.method == 'GET':
        return render_template('Cadastro.html')
    elif request.method == 'POST':
        # Recebo o request que foi pego do meu formulário
        x = request.form.get('X')
        y = request.form.get('Y')
        z = request.form.get('Z')
        r = request.form.get('R')

        dbCaminhos.insert({'x': x, 'y': y, 'z': z, 'r': r})


@app.route("/pegar_caminho", methods=['GET', 'POST'])
def pegar_caminho():
    if request.method == 'GET':
        return render_template('PegarCaminho.html')
    elif request.method == 'POST':
        # Receber um id e retornar o caminho
        id = request.form.get('id')
        caminho = dbCaminhos.get(doc_id=int(id))

        if caminho is None:
            return render_template('PegarCaminho.html', caminho='Caminho não encontrado')
        else:
            return render_template('PegarCaminho.html', caminho=caminho)
    






# Tendo o run não precisamos passar os parametrso do servidor pelo terminal basta rodar o arquivo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)