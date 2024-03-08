from flask import Flask, render_template, request, redirect, url_for, session, flash
from tinydb import TinyDB, Query

# Instaciando servidor em Flask
app = Flask(__name__)

# Instanciando o banco de dados
dbCaminhos = TinyDB('src/caminhos.json', indent=4)

# Configuração para recarregar os templates (Páginas HTML) automaticamente
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=['GET'])
def index():
    return render_template('Index.html')

# Rota para a página de cadastrar um novo caminho
@app.route("/novo", methods=['GET', 'POST'])
def novo():
    # Se o método for GET, renderiza a página de cadastro
    if request.method == 'GET':
        return render_template('Cadastro.html')
    # Se o método for POST, pega os dados do formulário e salva no banco de dados
    elif request.method == 'POST':
        # Recebo o request que foi pego do meu formulário
        x = request.form.get('X')
        y = request.form.get('Y')
        z = request.form.get('Z')
        r = request.form.get('R')

        dbCaminhos.insert({'x': x, 'y': y, 'z': z, 'r': r})

        return render_template('Cadastro.html', mensagem='Caminho cadastrado com sucesso')

# Rota para a página de pegar um caminho
@app.route("/pegar_caminho", methods=['GET', 'POST'])
def pegar_caminho():
    # Se o método for GET, renderiza a página de pegar caminho
    if request.method == 'GET':
        return render_template('PegarCaminho.html')
    elif request.method == 'POST':
        # Receber um id e retornar o caminho
        id = request.form.get('id')
        caminho = dbCaminhos.get(doc_id=int(id))

        # Se o caminho não existir, retornar uma mensagem
        if caminho is None:
            return render_template('PegarCaminho.html', caminho='Caminho não encontrado')
        else:
            return render_template('PegarCaminho.html', caminho=caminho)

# Rota para a página de listar os caminhos
@app.route("/listar_caminhos", methods=['GET'])
def listar_caminhos():
    # Quero listar caminhos que estão no banco de dados
    caminhos = dbCaminhos.all()
    # Pegar o id de cada caminho
    resposta_caminhos = []

    for caminho in caminhos:
        caminho['id'] = caminho.doc_id
        resposta_caminhos.append(caminho)

    
    return render_template('ListarCaminhos.html', caminhos=resposta_caminhos)

# Rota para a página de atualizar um caminho
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
        
        # Atualizar o caminho com o id passado
        dbCaminhos.update({'x': x, 'y': y, 'z': z, 'r': r}, doc_ids=[int(id)]) # Estou usando o doc_ids para atualizar o caminho com o id passado

        return render_template('atualizar.html', mensagem='Caminho com id: ' + str(id) +  ' atualizado com sucesso')
    
# Rota para a página de deletar um caminho
@app.route("/deletar", methods=['GET', 'POST'])
def deletar():
    if request.method == 'GET':
        return render_template('Deletar.html')
    elif request.method == 'POST':
        id = request.form.get('id')
        
        # Deletar o caminho com o id passado
        dbCaminhos.remove(doc_ids=[int(id)])
        
        return render_template('Deletar.html', mensagem='Caminho com id:' + str(id) +  'deletado com sucesso')

# Tendo o run não precisamos passar os parametrso do servidor pelo terminal basta rodar o arquivo
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)