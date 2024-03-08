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
    
@app.route("/listar_caminhos", methods=['GET'])
def listar_caminhos():
    caminhos = dbCaminhos.all()
    return render_template('ListarCaminhos.html', caminhos=caminhos)

@app.route("/atualizar", methods=['GET', 'POST'])
def atualizar():
    if request.method == 'GET':
        return render_template('Atualizar.html')
    elif request.method == 'POST':
        id = request.form.get('id')
        x = request.form.get('X')
        y = request.form.get('Y')
        z = request.form.get('Z')
        r = request.form.get('R')

        dbCaminhos.update({'x': x, 'y': y, 'z': z, 'r': r}, doc_ids=[int(id)])

        return redirect(url_for('listar_caminhos'))
    
@app.route("/deletar", methods=['GET', 'POST'])
def deletar():
    if request.method == 'GET':
        return render_template('Deletar.html')
    elif request.method == 'POST':
        id = request.form.get('id')
        
        dbCaminhos.remove(doc_ids=[int(id)])
        
        return render_template('Deletar.html', mensagem='Caminho com id:' + str(id) +  'deletado com sucesso')

# Tendo o run não precisamos passar os parametrso do servidor pelo terminal basta rodar o arquivo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)