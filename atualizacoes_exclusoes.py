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

if __name__ == "__main__":
    
    print("Marcando livro como devolvido...")
    marcar_livro_como_devolvido(1)

    print("Removendo autor...")
    remover_autor("J.K. Rowling")

    print("Atualizando disponibilidade do exemplar...")
    atualizar_disponibilidade_exemplar(2, True)

    print("Excluindo livro...")
    excluir_livro("A Arte de Vender Bem")
