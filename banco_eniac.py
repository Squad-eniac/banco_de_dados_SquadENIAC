import sqlite3

conexao = sqlite3.connect('banco_eniac')
cursor = conexao.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')

#tabela Pessoa
cursor.execute('CREATE TABLE IF NOT EXISTS Pessoa(id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100) NOT NULL)')

#tabela Autor (herda de Pessoa)
cursor.execute('CREATE TABLE IF NOT EXISTS Autor(id_autor INTEGER PRIMARY KEY,FOREIGN KEY (id_autor) REFERENCES Pessoa (id_pessoa))')

#tabela Usuário (herda de Pessoa)
cursor.execute('CREATE TABLE IF NOT EXISTS Usuario(id_usuario INTEGER PRIMARY KEY,telefone VARCHAR(100),nacionalidade VARCHAR(100),FOREIGN KEY(id_usuario) REFERENCES Pessoa (id_pessoa))')

#tabela Livro
cursor.execute('CREATE TABLE IF NOT EXISTS Livro(id_livro INTEGER PRIMARY KEY AUTOINCREMENT,titulo VARCHAR(100) NOT NULL,editora VARCHAR(100),max_renovacoes INTEGER)')

#tabela Gênero
cursor.execute('CREATE TABLE IF NOT EXISTS Genero(id_genero INTEGER PRIMARY KEY AUTOINCREMENT,genero VARCHAR(100) NOT NULL)')


conexao.commit()
conexao.close()