# Prova 1 - Módulo 5

Nome: Rodrigo Sales Freire dos Santos

## Instruções para execução do projeto

1. Clonar repositorio
2. Criar ambiente virtual
   1. python -m venv venv
   2. Linux: source venv/bin/activate | Windows: venv\Scripts\activate
3. Instalar dependências
   1. pip install -r requirements.txt
4. Executar o arquivo app.py
   1. python src/app.py
5. Acessar o endereço fornecido pelo flask


## Estrutura do projeto

p1-M05
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
└── src
    ├── app.py
    ├── caminhos.json
    └── templates
        ├── Deletar.html
        ├── Atualizar.html
        ├── ListarCaminhos.html
        ├── PegarCaminho.html
        ├── index.html
        └── Cadastro.html

Dentro da pasta src, temos o arquivo app.py, que é onde está o servidor da aplicação. Ele é responsável criar as rotas da aplicação. O arquivo caminhos.json é o banco de dados do sistema, onde são armazenados os caminhos. A pasta templates contém os arquivos html que são renderizados pelo flask.