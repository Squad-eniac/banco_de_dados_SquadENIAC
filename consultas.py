import sqlite3

# função para listar todos os livros na biblioteca, independente de cópias disponíveis ou não
def listar_livros_disponiveis():
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT l.titulo 
        FROM Livro l  -- Corrigido para 'l' minúsculo
        JOIN Exemplar e ON l.id_livro = e.id_livro
        WHERE e.disponivel = True;
    ''')

    livros_disponiveis = cursor.fetchall()
    conexao.close()

    return livros_disponiveis

#  função para listar todos os livros emprestados
def encontrar_livros_emprestados():
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT l.titulo 
        FROM Livro l
        JOIN Exemplar e ON l.id_livro = e.id_livro
        JOIN Emprestimo em ON e.id_exemplar = em.id_exemplar
        WHERE em.status = 'Em aberto';
    ''')

    livros_emprestados = cursor.fetchall()
    conexao.close()

    return livros_emprestados

# função para listar todos os livros de um autor específico
def localizar_livros_por_autor(nome_autor):
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT l.titulo 
        FROM Livro l
        JOIN Livro_Autor la ON l.id_livro = la.id_livro
        JOIN Autor a ON la.id_autor = a.id_autor
        JOIN Pessoa p ON a.id_autor = p.id_pessoa
        WHERE p.nome = ?;
    ''', (nome_autor,))

    livros_por_autor = cursor.fetchall()
    conexao.close()

    return livros_por_autor

# função para contar quantas cópias de um livro específico
def verificar_copias_disponiveis(titulo_livro):
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT l.titulo, COUNT(*) AS copias_disponiveis
        FROM Livro l
        JOIN Exemplar e ON l.id_livro = e.id_livro
        WHERE l.titulo = ?
        AND e.disponivel = True
        GROUP BY l.titulo;
    ''', (titulo_livro,))

    resultado = cursor.fetchone()
    conexao.close()

    if resultado:
        return resultado
    else:
        return None 

# função para listar os empréstimos atrasados
def mostrar_emprestimos_em_atraso():
    conexao = sqlite3.connect('banco_eniac')
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT em.id_emprestimo, p.nome AS usuario, l.titulo, em.data_devolucao
        FROM Emprestimo em
        JOIN Exemplar e ON em.id_exemplar = e.id_exemplar
        JOIN Livro l ON e.id_livro = l.id_livro
        JOIN Usuario u ON em.id_usuario = u.id_usuario
        JOIN Pessoa p ON u.id_usuario = p.id_pessoa
        WHERE em.status = 'Em aberto'
        AND em.data_devolucao < DATE('now'); 
    ''')

    emprestimos_em_atraso = cursor.fetchall()
    conexao.close()

    return emprestimos_em_atraso

if __name__ == "__main__":
    # Exemplos de uso das funções de consulta

    print("Livros disponíveis:")
    for livro in listar_livros_disponiveis():
        print(livro[0])

    print("\nLivros emprestados:")
    for livro in encontrar_livros_emprestados():
        print(livro[0])

    print("\nLivros de J.K. Rowling:")
    for livro in localizar_livros_por_autor("J.K. Rowling"):
        print(livro[0])

    resultado = verificar_copias_disponiveis("A Arte de Vender Bem")
    if resultado:
        print(f"\n{resultado[0]}: {resultado[1]} cópias disponíveis")
    else:
        print("\nLivro não encontrado ou sem cópias disponíveis")

    print("\nEmpréstimos em atraso:")
    for emprestimo in mostrar_emprestimos_em_atraso():
        print(f"ID: {emprestimo[0]}, Usuário: {emprestimo[1]}, Livro: {emprestimo[2]}, Data de Devolução: {emprestimo[3]}")
        