# p1-M05

O seu sistema deve, obrigatoriamente, utilizar o TinyDB para armazenar os dados. Eles devem ficar em um arquivo chamado caminhos.json. O usuário deve conseguir visualizar os caminhos que já foram cadastrados, modificar e deletar estes caminhos. Cada ponto armazenado deve ser representado por suas coordenadas: x, y, z e r. O seu sistema deve fornecer, no mínimo, as seguintes rotas:

●      /novo: cadastrar um novo conjunto de pontos em um caminho

●      /pegar_caminho: recebe o id do caminho e devolve os pontos cadastrados nele

●      /listas_caminhos: retorna o id e o nome de todos os caminhos cadastrados

●      /atualizar: atualiza o caminho cujo id foi fornecido

●      /deletar: deleta o caminho com o id fornecido