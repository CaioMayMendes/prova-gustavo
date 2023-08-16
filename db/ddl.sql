start transaction
;

CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL
);

CREATE TABLE endereco (
    id_endereco SERIAL PRIMARY KEY,
    id_usuario INTEGER REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    descricao VARCHAR(255) NOT NULL,
    cep VARCHAR(10) NOT NULL,
    rua VARCHAR(255) NOT NULL,
    complemento VARCHAR(255),
    bairro VARCHAR(255) NOT NULL,
    cidade VARCHAR(255) NOT NULL,
    estado VARCHAR(2) NOT NULL
);

CREATE TABLE categoria (
    id_categoria SERIAL PRIMARY KEY,
    nome VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE produto (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE produto_categoria (
    id_produto INTEGER REFERENCES produto(id_produto) ON DELETE CASCADE,
    id_categoria INTEGER REFERENCES categoria(id_categoria) ON DELETE CASCADE,
    PRIMARY KEY (id_produto, id_categoria)
);

CREATE TABLE pedido (
    id_pedido SERIAL PRIMARY KEY,
    id_usuario INTEGER REFERENCES usuario(id_usuario) ON DELETE CASCADE,
    id_endereco INTEGER REFERENCES endereco(id_endereco) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL,
    data_pedido TIMESTAMP NOT NULL,
    CHECK (status IN ('Pendente', 'Pago', 'Enviado', 'Entregue', 'Cancelado'))
);

CREATE TABLE itens_pedido (
    id_itens_pedido SERIAL PRIMARY KEY,
    id_pedido INTEGER REFERENCES pedido(id_pedido) ON DELETE CASCADE,
    id_produto INTEGER REFERENCES produto(id_produto) ON DELETE CASCADE,
    preco DECIMAL(10, 2) NOT NULL,
    quantidade INTEGER NOT NULL
);

commit
;