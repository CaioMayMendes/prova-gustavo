# Prova Prática Desenvolvedor Backend Python - Ganimedes

Olá Gustavo! :)

Obrigado pelo seu compromentimento com a nossa equipe!

Leia atentamente as informações abaixo para realização da prova.

Boa prova!!

## Descrição da prova

Você deve criar uma API em Python usando o framework FastAPI. 

A API deve ser capaz de receber requisições HTTP e retornar respostas no formato JSON. 

A API deve permitir a criação, leitura, atualização e exclusão (CRUD) de recursos em um banco de dados PostgreSQL.

## Banco de dados

Dentro da pasta `db` tem o arquivo `ddl.sql` com a estrutura das tabelas, só executar em um banco de dados criado local.

Dentro da pasta `core` tem o arquivo `settings.py` que você vai configurar o caminho da conexão com o banco de dados.

## Requisitos funcionais

- A API deve permitir o cadastro de usuários com nome, e-mail e senha. 
## Criei já para você ter um exemplo de como seguir com os outros itens

- A API deve permitir que seja cadastrado um ou mais endereços para um mesmo usuário. Os campos do endereço são: descrição, cep, logradouro, complemento, bairro, cidade e estado.
- A API deve permitir o cadastro de categorias de produtos com nome.
- A API deve permitir o cadastro de produtos com nome, descrição e preço. Um produto pode ter uma ou mais categorias associadas.
- A API deve permitir a criação de pedidos associados a um usuário. Cada pedido terá status, data e conterá um ou mais produtos com seu respectivo preço e quantidade. Além disso, cada pedido será vinculado a um dos endereços do usuário.

- A API deve permitir a consulta de usuários cadastrados.
- A API deve permitir a consulta de produtos cadastrados.
- A API deve permitir a consulta de endereços de um usuário.
- A API deve permitir a consulta de pedidos de um usuário, retornando uma lista dos produtos, seus preços e o valor total do pedido e o endereço do usuário.

## Dicas
- Pra cada arquivo que você criar dentro da pasta api você vai ter que adicionar uma nova linha no arquivo `__init__.py` dentro da pasta api.
- No retorno de algo que retorne mais de um item se atente na responde_model em colocar o tipo List.
- Caso queira ver mais dados para usar de base, utilize o nosso projeto já existe da Uleader pois segue o mesmo padrão.