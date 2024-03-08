# p1-M05

O seu sistema deve, obrigatoriamente, utilizar o TinyDB para armazenar os dados. Eles devem ficar em um arquivo chamado caminhos.json. O usuário deve conseguir visualizar os caminhos que já foram cadastrados, modificar e deletar estes caminhos. Cada ponto armazenado deve ser representado por suas coordenadas: x, y, z e r. O seu sistema deve fornecer, no mínimo, as seguintes rotas:

●      /novo: cadastrar um novo conjunto de pontos em um caminho

●      /pegar_caminho: recebe o id do caminho e devolve os pontos cadastrados nele

●      /listas_caminhos: retorna o id e o nome de todos os caminhos cadastrados

●      /atualizar: atualiza o caminho cujo id foi fornecido

●      /deletar: deleta o caminho com o id fornecido


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
        └── Cadastro.html

Dentro da pasta src, temos o arquivo app.py, que é onde está o servidor da aplicação. Ele é responsável criar as rotas da aplicação. O arquivo caminhos.json é o banco de dados do sistema, onde são armazenados os caminhos. A pasta templates contém os arquivos html que são renderizados pelo flask.