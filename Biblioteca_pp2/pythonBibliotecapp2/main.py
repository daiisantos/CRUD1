import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "ifpecjbg",
    database="biblioteca_pp2"
)

if conexao.is_connected():
    print("Conexão ao MySQL bem-sucedida!")
    cursor = conexao.cursor()


def exibir_menu():
    print('''

   ---- Escolha uma opção: ----
   
    1.  Cadastrar Autor 
    2.  Listar Autores
    3.  Procurar Autor
    4.  Alterar Autor
    5.  Excluir Autor
    6.  Cadastrar livro
    7.  Listar livros
    8.  Procurar livro
    9.  Alterar livro
    10. Excluir livro
    11. Cadastrar Cliente
    12. Listar Clientes
    13. Procurar Cliente
    14. Alterar Cliente
    15. Excluir Cliente
    16. Adicionar ao estoque
    17. Listar estoque
    18. Atualizar estoque
    19. Excluir do estoque
    20. Emprestimo
    21. Listar emprestimo
    22. Devolver livro
    99. Buscar livro pelo título
    0.  Sair
    ''')


#########AUTOR


def getAutor():
    cursor.execute("select concat(id, ' - ', nome) from autor")
    for linha in cursor.fetchall():
        print(linha)


def cadastrarAutor():
    autor = input("Digite o nome do autor: ")
    cursor.execute(
        f"INSERT INTO autor (nome) VALUES ('{autor}');")
    conexao.commit()


def buscarAutor():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"select concat(id, ' - ', nome) from autor where id = {identificador_desejado}")
    print(cursor.fetchall())


def exibirMenuAtualizarAutor():
    print('''

      Escolha uma opção:

      1. Atualizar nome do autor
      0. sair

      ''')


def atualizarAutor():
    opcao = 1
    identificador_desejado = int(input('id? '))
    cursor.execute(f"select * from autor where id = {identificador_desejado}")
    print(cursor.fetchall())
    while opcao != 0:
        exibirMenuAtualizarAutor()
        opcao = int(input("Opção: "))
        if opcao == 1:
            novoNome_Autor = input("Digite o Nome do Autor")
            cursor.execute(f"update autor set nome = '{novoNome_Autor}' where id = {identificador_desejado}")
            conexao.commit()
        elif opcao == 0:
            break
        else:
            print("Opção inválida")


def apagarAutor():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"delete from autor where id = {identificador_desejado}")
    conexao.commit()


#########LIVROS
def getLivros():
    cursor.execute("select concat(id, ' - ', titulo) from livro")
    for linha in cursor.fetchall():
        print(linha)


def buscarLivro():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"select concat(id, ' - ', titulo) from livro where id = {identificador_desejado}")
    print(cursor.fetchall())


def buscarLivroNome():
    nome_desejado = input('Digite o título do livro:  ')
    cursor.execute(f"select concat(id, ' - ', titulo) from livro where titulo like '%{nome_desejado}%'")
    print(cursor.fetchall())

def cadastrarLivro():
    titulo = input("Digite o título do livro: ")
    autorId = int(input("Digite o id do autor: "))
    data = input("Digite uma data no formato (YYYY-MM-DD) : ")
    cursor.execute(
        f"INSERT INTO livro (autor_id, titulo, data_lancamento) VALUES ('{autorId}', '{titulo}', '{data}');")
    conexao.commit()


def apagarLivro():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"delete from livro where id = {identificador_desejado}")
    conexao.commit()


def exibirMenuAtualizarLivro():
    print('''

      Escolha uma opção:

      1. Atualizar título
      2. Atualizar Autor
      3. Atualizar Data
      0. sair
      ''')


def atualizarLivro():
    opcao = 1
    identificador_desejado = int(input('id? '))
    cursor.execute(f"select * from livro where id = {identificador_desejado}")
    print(cursor.fetchall())
    while opcao != 0:
        exibirMenuAtualizarLivro()
        opcao = int(input("Opção: "))
        if opcao == 1:
            titulo = input("Digite o título")
            cursor.execute(f"update livro set titulo = '{titulo}' where id = {identificador_desejado}")
            conexao.commit()
        elif opcao == 2:
            autor_id = int(input("Digite o id do autor"))
            cursor.execute(f"update livro set autor_id = {autor_id} where id = {identificador_desejado}")
            conexao.commit()
        elif opcao == 3:
            data = input("Digite uma data no formato (YYYY-MM-DD) : ")
            cursor.execute(f"update livro set data_lancamento = '{data}' where id = {identificador_desejado}")
            conexao.commit()
        elif opcao == 0:
            break
        else:
            print("opção invalida")



########Cliente
def cadastrarCliente():
    cliente = input("Digite o nome do Cliente: ")
    cpfCliente = input("Qual o CPF do cliente?")
    cursor.execute(
        f"INSERT INTO cliente (nome, cpf) VALUES ('{cliente}', '{cpfCliente}');")
    conexao.commit()


def getCliente():
    cursor.execute("select concat(id, ' - ', nome) from cliente")
    for linha in cursor.fetchall():
        print(linha)


def buscarCliente():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"select concat(id, ' - ', nome) from cliente where id = {identificador_desejado}")
    print(cursor.fetchall())


def exibirMenuAtualizarCliente():
    print('''

      Escolha uma opção:

      1. Atualizar nome do Cliente
      2. Atualizar CPF
      0. sair

      ''')


def atualizarCliente():
    opcao = 1
    identificador_desejado = int(input('id? '))
    cursor.execute(f"select * from cliente where id = {identificador_desejado}")
    print(cursor.fetchall())
    while opcao != 0:
        exibirMenuAtualizarCliente()
        opcao = int(input("Opção: "))
        if opcao == 1:
            novoNome_Cliente = input("Digite o Nome do Cliente")
            cursor.execute(f"update Cliente set nome = '{novoNome_Cliente}' where id = {identificador_desejado}")
            conexao.commit()
        elif opcao == 2:
            novoCpf = input("Digite o CPF")
            cursor.execute(f"update Cliente set cpf = '{novoCpf}' where id = {identificador_desejado}")
            conexao.commit()
        elif opcao == 0:
            break
        else:
            print("Opção inválida")


def apagarCliente():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"delete from cliente where id = {identificador_desejado}")
    conexao.commit()


############Estoque
def cadastrarEstoque():
    livro_id = int(input('Digite o id do livro: '))
    quantidade = int(input('Digite a quantidade em estoque: '))
    cursor.execute(
        f"INSERT INTO estoque (livro_id, quantidade) VALUES ('{livro_id}', '{quantidade}');")

def getEstoque():
    cursor.execute("select concat(estoque.id, ' - ',livro.titulo, ' - quantidade: ', estoque.quantidade) from estoque join livro on livro.id = estoque.livro_id")
    for linha in cursor.fetchall():
        print(linha)

def atualizarEstoque():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"select concat(livro.titulo, ' - quantidade: ', estoque.quantidade) from estoque join livro on livro.id = estoque.livro_id where estoque.id = {identificador_desejado}") #join= juntar tabela
    print(cursor.fetchall())
    quantidade = int(input('nova quantidade? '))
    cursor.execute(f"update estoque set quantidade = '{quantidade}' where id = {identificador_desejado}")
    conexao.commit()

def apagarEstoque():
    identificador_desejado = int(input('id? '))
    cursor.execute(f"delete from estoque where id = {identificador_desejado}")
    conexao.commit()

#######EMPRESTAR

def emprestar():
    identificador_cliente = int(input('id do cliente:  '))
    identificador_livro = int(input('id do livro:  '))

    cursor.execute(f"update estoque join livro on estoque.livro_id = livro.id set estoque.quantidade = estoque.quantidade - 1 where estoque.livro_id = {identificador_livro}")
    cursor.execute(f"INSERT INTO emprestimo (livro_id, cliente_id) VALUES ('{identificador_livro}', '{identificador_cliente}');")
    conexao.commit()

def getemprestimos():
    cursor.execute("select cliente.nome, livro.titulo from emprestimo join  livro on livro.id = emprestimo.livro_id join cliente on cliente.id = emprestimo.cliente_id")
    for linha in cursor.fetchall():
        print(linha)

def devolver():
    identificador_cliente = int(input('id do cliente:  '))
    identificador_livro = int(input('id do livro:  '))

    cursor.execute(f"update estoque join livro on estoque.livro_id = livro.id set estoque.quantidade = estoque.quantidade + 1 where estoque.livro_id = {identificador_livro}")
    cursor.execute(f"DELETE from emprestimo where emprestimo.livro_id = {identificador_livro} and emprestimo.cliente_id = {identificador_cliente};")
    conexao.commit()

def main():
    print('iniciando programa')

    opcao = 1
    while opcao != 0:
        exibir_menu()
        opcao = int(input("Opção: "))
        if opcao == 1:
            cadastrarAutor()
        elif opcao == 2:
            getAutor()
        elif opcao == 3:
            buscarAutor()
        elif opcao == 4:
            atualizarAutor()
        elif opcao == 5:
            apagarAutor()
        elif opcao == 6:
            cadastrarLivro()
        elif opcao == 7:
            getLivros()
        elif opcao == 8:
            buscarLivro()
        elif opcao == 9:
            atualizarLivro()
        elif opcao == 10:
            apagarLivro()
        elif opcao == 11:
            cadastrarCliente()
        elif opcao == 12:
            getCliente()
        elif opcao == 13:
            buscarCliente()
        elif opcao == 14:
            atualizarCliente()
        elif opcao == 15:
            apagarCliente()
        elif opcao == 16:
            cadastrarEstoque()
        elif opcao == 17:
            getEstoque()
        elif opcao == 18:
            atualizarEstoque()
        elif opcao == 19:
            apagarEstoque()
        elif opcao == 20:
            emprestar()
        elif opcao == 21:
            getemprestimos()
        elif opcao == 22:
            devolver()
        elif opcao == 99:
            buscarLivroNome()
        elif opcao == 0:
            break
        else:
            print("opção invalida")




main()
