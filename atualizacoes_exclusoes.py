import sqlite3

 # Marca um livro como devolvido atualizando o status do empréstimo e a data de devolução
def marcar_livro_como_devolvido(id_emprestimo):   
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE Emprestimo
        SET status = 'Devolvido', data_devolucao = DATE('now')
        WHERE id_emprestimo = ?;
    ''', (id_emprestimo,))

    conexao.commit()
    conexao.close()

# Remove um autor do banco de dados, incluindo registros relacionados na tabela Autor
def remover_autor(nome_autor):    
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM Autor
        WHERE id_autor IN (
            SELECT a.id_autor
            FROM Autor a
            JOIN Pessoa p ON a.id_autor = p.id_pessoa
            WHERE p.nome = ?
        );
    ''', (nome_autor,))

    conexao.commit()
    conexao.close()

# Atualiza a disponibilidade de um exemplar específico
def atualizar_disponibilidade_exemplar(id_exemplar, disponivel):    
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE Exemplar
        SET disponivel = ?
        WHERE id_exemplar = ?;
    ''', (disponivel, id_exemplar))

    conexao.commit()
    conexao.close()

# Exclui um livro do banco de dados com base no título
def excluir_livro(titulo_livro):    
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM Livro
        WHERE titulo = ?;
    ''', (titulo_livro,))

    conexao.commit()
    conexao.close()

# Atualiza o número de renovações de um empréstimo
def atualizar_numero_renovacoes(id_exemplar, novas_renovacoes):
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE Exemplar
        SET num_atual_renovacoes = ?
        WHERE id_exemplar = ?;
    ''', (novas_renovacoes, id_exemplar))

    conexao.commit()
    conexao.close()

# Remove um gênero do banco de dados
def remover_genero(nome_genero):
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM Genero
        WHERE genero = ?;
    ''', (nome_genero,))

    conexao.commit()
    conexao.close()

# Atualiza a editora de um livro específico
def atualizar_editora_livro(titulo_livro, nova_editora):
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE Livro
        SET editora = ?
        WHERE titulo = ?;
    ''', (nova_editora, titulo_livro))

    conexao.commit()
    conexao.close()

# Remove um usuário do banco de dados
def remover_usuario(nome_usuario):
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        DELETE FROM Usuario
        WHERE id_usuario IN (
            SELECT u.id_usuario
            FROM Usuario u
            JOIN Pessoa p ON u.id_usuario = p.id_pessoa
            WHERE p.nome = ?
        );
    ''', (nome_usuario,))

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    
    print("Marcando livro como devolvido...")
    marcar_livro_como_devolvido(1)

    print("Removendo autor...")
    remover_autor("J.K. Rowling")

    print("Atualizando disponibilidade do exemplar...")
    atualizar_disponibilidade_exemplar(2, True)

    print("Excluindo livro...")
    excluir_livro("A Arte de Vender Bem")

    print("Atualizando número de renovações...")
    atualizar_numero_renovacoes(3, 2)

    print("Removendo gênero...")
    remover_genero("Ficção Científica")

    print("Atualizando editora do livro...")
    atualizar_editora_livro("A Arte de Vender Bem", "Nova Editora")

    print("Removendo usuário...")
    remover_usuario("Marília Gonçalves")

   