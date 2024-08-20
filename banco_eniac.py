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
cursor.execute('CREATE TABLE IF NOT EXISTS Livro(id_livro INTEGER PRIMARY KEY AUTOINCREMENT,titulo VARCHAR(100) NOT NULL,editora VARCHAR(100),max_renovacoes INTEGER DEFAULT 3)')

#tabela Gênero
cursor.execute('CREATE TABLE IF NOT EXISTS Genero(id_genero INTEGER PRIMARY KEY AUTOINCREMENT,genero VARCHAR(100) NOT NULL)')

#tabela Exemplar (herda de Livro)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Exemplar (
        id_exemplar INTEGER PRIMARY KEY AUTOINCREMENT,
        id_livro INTEGER NOT NULL,
        disponivel BOOLEAN,
        num_atual_renovacoes INTEGER,
        FOREIGN KEY(id_livro) REFERENCES Livro(id_livro)
    )
''')

#tabela Empréstimo
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Emprestimo (
        id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
        id_exemplar INTEGER NOT NULL,
        id_usuario INTEGER NOT NULL,
        data_emprestimo DATE NOT NULL,
        data_devolucao DATE,
        status VARCHAR(100),
        FOREIGN KEY(id_exemplar) REFERENCES Exemplar(id_exemplar),
        FOREIGN KEY(id_usuario) REFERENCES Usuario(id_usuario)
    )
''')

#tabela Livro_Genero (associativa entre Livro e Genero)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livro_Genero (
        id_livro INTEGER NOT NULL,
        id_genero INTEGER NOT NULL,
        PRIMARY KEY(id_livro, id_genero),
        FOREIGN KEY(id_livro) REFERENCES Livro(id_livro),
        FOREIGN KEY(id_genero) REFERENCES Genero(id_genero)
    )
''')

#tabela Livro_Autor (associativa entre Livro e Autor)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livro_Autor (
        id_livro INTEGER NOT NULL,
        id_autor INTEGER NOT NULL,
        PRIMARY KEY(id_livro, id_autor),
        FOREIGN KEY(id_livro) REFERENCES Livro(id_livro),
        FOREIGN KEY(id_autor) REFERENCES Autor(id_autor)
    )
''')

conexao.commit()
conexao.close()