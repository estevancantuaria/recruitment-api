CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT(50) NOT NULL,
    email TEXT(50) NOT NULL UNIQUE,
    senha TEXT(50) NOT NULL,
    cpf TEXT(50) NOT NULL UNIQUE,
    telefone TEXT(50) NOT NULL UNIQUE,
    ativo BOOLEAN NOT NULL,
    tipo_usuario TEXT(50) NOT NULL
);

CREATE TABLE jovens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    rg TEXT(50) NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE recrutadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    empresa TEXT(50) NOT NULL,
    cargo TEXT(50) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE endereco (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    rua TEXT(100) NOT NULL,
    numero TEXT(10) NOT NULL,
    complemento TEXT(50),
    bairro TEXT(50),
    cidade TEXT(50) NOT NULL,
    estado TEXT(50) NOT NULL,
    cep TEXT(20) NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE escolaridade (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    nivel TEXT(50) NOT NULL, -- Ex: Ensino Fundamental, Ensino Médio, Graduação, etc.
    instituicao TEXT(100) NOT NULL,
    ano_conclusao INTEGER,
    periodo_serie TEXT(50), -- Ex: 1º ano, 2º semestre, etc.
    FOREIGN KEY(user_id) REFERENCES users(id)
);



