import sqlite3
import registros

conexao = sqlite3.connect('banco_eniac')
cursor = conexao.cursor()

cursor.execute('PRAGMA foreign_keys = ON;')


# Inserindo dados tabela pessoa
# Pessoa(id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,nome VARCHAR(100) NOT NULL)')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Isadora Maria") ') (1º de teste)
# Adicionando mais 10 dados de exemplo
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Gabriela Pessoa") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Marília Gonçalves") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Jaqueline Rosa") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Rosa Viana") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Roseli Vieira") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Ana Clara Nogueira") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Marcela Afonso") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Luana Vieira") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Angelo Souza") ')
# cursor.execute('INSERT INTO Pessoa(nome) VALUES("Rafael Silva") ')

# Inserindo dados na tabela Usuario (herda de Pessoa)
# Usuario(id_usuario INTEGER PRIMARY KEY,telefone VARCHAR(100),nacionalidade VARCHAR(100),FOREIGN KEY(id_usuario) REFERENCES Pessoa (id_pessoa))')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(1, "123456789", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(2, "987654321", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(3, "456789123", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(4, "321654987", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(5, "654987321", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(6, "789123456", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(7, "147258369", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(8, "963852741", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(9, "852963741", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(10, "741852963", "Brasileira")')
# cursor.execute('INSERT INTO Usuario(id_usuario, telefone, nacionalidade) VALUES(11, "369147852", "Brasileira")')

# Inserindo dados na tabela Livro
# Livro(id_livro INTEGER PRIMARY KEY AUTOINCREMENT,titulo VARCHAR(100) NOT NULL,editora VARCHAR(100),max_renovacoes INTEGER DEFAULT 3)')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("A Arte de Vender Bem", "Siciliano")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("A Arte de Falar Bem", "Siciliano")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("Banco de Dados para Iniciantes", "Programe")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("Python para Principiantes", "DataHouse")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("A Viagem de Chihiro", "Rumi Hiiragi")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("A Arte da Gurra", "Sun Tzu")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("A Coragem de Ser Imperfeito", "Brene Brown")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("12 Regras para a Vida", "Jordan Peterson")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("As Valkirias", "Paulo Coelho")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("O Senhor dos Aneis I", "J R R Tolkien")')
# cursor.execute('INSERT INTO Livro(titulo,editora) VALUES("O Senhor dos Aneis II", "J R R Tolkien")')

# Inserção de dados na tabela Gênero
# Genero(id_genero INTEGER PRIMARY KEY AUTOINCREMENT,genero VARCHAR(100) NOT NULL)')
# Inserindo dados na tabela Genero
# cursor.execute('INSERT INTO Genero(genero) VALUES("Ficção Científica")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Romance")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Mistério")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Biografia")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("História")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Fantasia")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Poesia")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Aventura")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Terror")')
# cursor.execute('INSERT INTO Genero(genero) VALUES("Autoajuda")')


# Inserindo registros de autores na tabela Pessoa
"""cursor.executemany('INSERT INTO Pessoa (nome) VALUES (?)', registros.pessoas_autores)"""

# Inserindo registros  na tabela Autor
"""cursor.executemany('INSERT INTO Autor (id_autor) VALUES (?)', registros.autores)"""

# Inserindo  registros na tabela Exemplar
"""cursor.executemany('''
    INSERT INTO Exemplar (id_livro, disponivel, num_atual_renovacoes) 
    VALUES (?, ?, ?)''', registros.exemplares)"""

# Inserindo registros na tabela  Emprestimo
"""cursor.executemany('''
INSERT INTO Emprestimo (id_exemplar, id_usuario, data_emprestimo, data_devolucao, status)
VALUES (?, ?, ?, ?, ?)''', registros.emprestimos)"""

# Inserindo registros na tabela Livro_Autor
"""cursor.executemany('''
INSERT INTO Livro_Autor (id_livro, id_autor)
VALUES (?, ?)''', registros.livro_autor)"""

# Inserindo registros na tabele Livro_Gênero
cursor.executemany('''
INSERT INTO Livro_Genero (id_livro, id_genero)
VALUES (?, ?)''', registros.livro_genero)


conexao.commit()
conexao.close()