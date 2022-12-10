from neo4j import GraphDatabase
import logging
from neo4j.exceptions import ServiceUnavailable

class App:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()
    
#  --------------------------------------------------------- Crud Usuario -----------------------------------------------------------------------------  

    def usuario(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.CriarUsuario)
    @staticmethod
    def CriarUsuario(db):
        query = ("CREATE (object: usuario {nome: $nomeUsuario, email: $emailUsuario, cpf: $cpfUsuario, endereco: $enderecoUsuario, telefone: $telefoneUsuario})")
        print("Iniciando Cadastramento de Usuario\n")
        nomeUsuario = input("Digite seu Nome: ")
        emailUsuario = input("Digite seu Email: ")
        cpfUsuario = input("Digite seu CPF: ")
        enderecoUsuario = input("Digite seu endereco: ")
        telefoneUsuario = input("Digite seu telefone: ")
        result = db.run(query, nomeUsuario=nomeUsuario, emailUsuario=emailUsuario, cpfUsuario=cpfUsuario, enderecoUsuario=enderecoUsuario, telefoneUsuario=telefoneUsuario)
        print("Usuário criado com sucesso!")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        return [{"object": row["object"]["nome"]["email"]["cpf"]["endereco"]["telefone"]} for row in result]

    def BuscarUsuarios(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self.BuscaUsuarios)
    @staticmethod
    def BuscaUsuarios(db):
        print("Iniciando Busca de Usuarios\n")
        query = "MATCH (u:usuario) RETURN u"
        result = db.run(query)
        return [print([row]) for row in result]

    def BuscarUsuarioCpf(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self.BuscarUsuarioEspecifico)
    @staticmethod
    def BuscarUsuarioEspecifico(db):
        cpfUsu = input("Insira o CPF do usuário que deseja encontrar: ")
        query = "MATCH (u:usuario) WHERE u.cpf = $cpfUsu RETURN u"
        result = db.run(query, cpfUsu=cpfUsu)
        return [print([row]) for row in result]

    def AtualizarUsuario(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.atualizarUsuario)
    @staticmethod
    def atualizarUsuario(db):
        cpfUusuario = input("Insira o CPF do usuário que deseja atualizar: ")
        print('''
                [1] - Nome
                [2] - Email
                [3] - CPF
                [4] - endereco
                [5] - telefone
            ''')
        escolha = input("Insira o número da opção que deseja atualizar: ")
        while int(escolha) < 1 or int(escolha) > 7:
            print("Opção inválida")
            escolha = input("Insira outra opção: ")
        if escolha   == "1": escolha = "nome"
        elif escolha == "2": escolha = "email"
        elif escolha == "3": escolha = "cpf"
        elif escolha == "4": escolha = "endereco"
        elif escolha == "5": escolha = "telefone"
        DadoAtualizado = input("Insira o novo valor: ")
        query = ("MATCH (u:usuario) WHERE u.cpf = $cpfUusuario SET u." + escolha + " = $DadoAtualizado")
        print("Usuário atualizado com sucesso!")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        db.run(query, cpfUusuario = cpfUusuario, escolha=escolha, DadoAtualizado=DadoAtualizado)

    def deleteUsuario(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self.deletarUsuario)
    @staticmethod
    def deletarUsuario(db):
        cpfUsuario = input("Insira o CPF do usuário a ser deletado: ")
        query = "MATCH (u:usuario) WHERE u.cpf = $cpfUsuario DETACH DELETE u"
        print("Usuário deletado")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        db.run(query, cpfUsuario=cpfUsuario)
    
#------------------------------------------------------------ Crud Vendedor -----------------------------------------------------------------------------  

    def CriarVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.CriaVendedor)
    @staticmethod
    def CriaVendedor(db):
        query = ("CREATE (object: vendedor {nome: $nomeVendedor, email: $emailVendedor, cnpj: $cnpjVendedor, endereco: $enderecoVendedor ,telefone: $telefoneVendedor})")
        print("Iniciando Cadastro Vendendor\n")
        nomeVendedor = input("Digite seu Nome: ")
        emailVendedor = input("Digite seu Email: ")
        cnpjVendedor = input("Digite seu CNPJ: ")
        enderecoVendedor = input("Digite seu endereco: ")
        telefoneVendedor = input("Digite seu telefone: ")
        result = db.run(query, nomeVendedor=nomeVendedor, emailVendedor=emailVendedor, cnpjVendedor=cnpjVendedor, enderecoVendedor=enderecoVendedor,telefoneVendedor=telefoneVendedor)
        print("Vendedor criado com sucesso!")
        print("------------------------------------------------------------------------------------------------")
        return [{"object": row["object"]["nome"]["email"]["cnpj"]["endereco"]["telefone"]} for row in result]

    def BuscarVendedores(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self.BuscaVendedor)
    @staticmethod
    def BuscaVendedor(db):
        print("Iniciando Busca de Vendedores\n")
        query = "MATCH (v:vendedor) RETURN v"
        result = db.run(query)
        return [print([row]) for row in result]

    def BuscarVendedorCnpj(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self.BuscarVendedorEspecifico)
    @staticmethod
    def BuscarVendedorEspecifico(db):
        cnpjVendedor = input("Insira o CNPJ do Vendedor que deseja encontrar: ")
        print("Iniciando Busca de Vendedores:")
        query = "MATCH (v:vendedor) WHERE v.cnpj = $cnpjVendedor RETURN v"
        result = db.run(query, cnpjVendedor=cnpjVendedor)
        return [print([row]) for row in result]

    def AtualizarVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.atualizarVendedor)
    @staticmethod
    def atualizarVendedor(db):
        cnpjVendedor = input("Insira o CNPJ do Vendedor que deseja atualizar: ")
        print('''
                [1] - Nome
                [2] - Email
                [3] - CPF
                [4] - endereco
                [5] - telefone
            ''')
        escolha = input("Insira o número da opção que deseja atualizar: ")
        while int(escolha) < 1 or int(escolha) > 7:
            print("Opção inválida")
            escolha = input("Insira outra opção: ")
        if escolha   == "1": escolha = "nome"
        elif escolha == "2": escolha = "email"
        elif escolha == "3": escolha = "cpf"
        elif escolha == "4": escolha = "endereco"
        elif escolha == "5": escolha = "telefone"
        DadoAtualizado = input("Insira o novo valor: ")
        query = ("MATCH (v:vendedor) WHERE v.cnpj = $cnpjVendedor SET v." + escolha + " = $DadoAtualizado")
        print("Vendedor atualizado com sucesso!")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        db.run(query, cnpjVendedor = cnpjVendedor, escolha=escolha, DadoAtualizado=DadoAtualizado)
        
    def deletarVendedor(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self.deleteVendedor)
    @staticmethod
    def deleteVendedor(db):
        cpfVendedor = input("Insira o CNPJ do Vendedor: ")
        query = "MATCH (v:vendedor) WHERE v.cnpj = $cpfVendedor DETACH DELETE v"
        print("Vendedor deletado")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        db.run(query, cpfVendedor=cpfVendedor)


#------------------------------------------------------------  Crud Produto -----------------------------------------------------------------------------  

    def CriarProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.CriacaoProduto)
    @staticmethod
    def CriacaoProduto(db):
        query = ("CREATE (object: produto {nome: $nomeProduto,emailSuporte: $emailSuporte, quantidade: $quantidadeProduto,Dataproducao: $DataProducao, preço: $precoProduto, vendedor: $cnpjVendedor})")
        print("Iniciando Cadastramento do Produto\n")
        nomeProduto          = input("Digite o Nome Do Produto: ")
        emailSuporte         = input("Digite o Email para Suporte do Produto: ")
        quantidadeProduto    = input("Digite a Quantidade Do Produto em Estoque: ")
        DataProducao         = input("Digite a Data de Produção do Produto: ")
        precoProduto         = input("Digite O Preço Do Produto: ")
        cnpjVendedor         = input("Digite O CNPJ do vendedor: ")
        result = db.run(query, nomeProduto=nomeProduto,emailSuporte=emailSuporte, quantidadeProduto=quantidadeProduto, DataProducao=DataProducao,precoProduto=precoProduto, cnpjVendedor=cnpjVendedor)
        print("Produto criado com sucesso!")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        return [{"object": row["object"]["nome"]["emailSuporte"]["quantidade"]["Dataproducao"]["preco"]["vendedor"]} for row in result]

    def BuscarProdutos(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self.buscaProdutos)
    @staticmethod
    def buscaProdutos(db):
        print("Iniciando Listagem de Produtos\n")
        query = "MATCH (p:produto) RETURN p"
        result = db.run(query)
        return [print([row]) for row in result]

    def BuscarProdutoEspecifico(self):
        with self.driver.session(database="neo4j") as session:
            session.read_transaction(self.BuscaEspecificaProduto)
    @staticmethod
    def BuscaEspecificaProduto(db):
        nomeProduto = input("Insira o nome do produto: ")
        query = "MATCH (p:produto) WHERE p.nome = $nomeProduto RETURN p"
        result = db.run(query, nomeProduto=nomeProduto)
        return [print([row]) for row in result]
    
    
    def deletarProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.write_transaction(self.deleteProduto)
    @staticmethod
    def deleteProduto(db):
        NomeProduto = input("Insira o Nome do Produto: ")
        query = "MATCH (p:produto) WHERE p.nome = $NomeProduto DETACH DELETE p"
        print("Produto deletado")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        db.run(query, NomeProduto=NomeProduto)

    def AtualizarProduto(self):
        with self.driver.session(database="neo4j") as session:
            session.execute_write(self.atualizaProduto)
    @staticmethod
    def atualizaProduto(db):
        nomeProduto = input("Insira o nome do Produto: ")
        print('''
                [1] - Nome
                [2] - EmailSuporte
                [3] - quantidadeProduto
                [4] - DataProducao
                [5] - precoProduto
                [6] - cnpjVendedor
            ''')
        escolha = input("Insira o número da opção que deseja atualizar: ")
        while int(escolha) < 1 or int(escolha) > 7:
            print("Opção inválida")
            escolha = input("Insira outra opção: ")
        if escolha   == "1": escolha = "nome"
        elif escolha == "2": escolha = "emailSuporte"
        elif escolha == "3": escolha = "quantidadeProduto"
        elif escolha == "4": escolha = "DataProducao"
        elif escolha == "5": escolha = "precoProduto"
        elif escolha == "5": escolha = "cnpjVendedor"
        DadoAtualizado = input("Insira o novo valor: ")
        query = ("MATCH (p:produto) WHERE p.nome = $nomeProduto SET p." + escolha + " = $DadoAtualizado")
        print("Produto atualizado com sucesso!")
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        db.run(query, nomeProduto = nomeProduto, escolha=escolha, DadoAtualizado=DadoAtualizado)


if __name__ == "__main__":
    uri = "neo4j+s://c244c55e.databases.neo4j.io"
    user = "neo4j"
    password = "ilyQmJ6tbh8No1CjUt6FkMFUYWg4o9kEg5bpMfjLpcs"
    app = App(uri, user, password)
    execucao = True
    while execucao:
        print('''Escolha Uma Opção:\n

--------------------  [ Usuario ]  --------------------  
    - [0]Parar Aplicacão\n
    - [1]Criar Usuario\n
    - [2]buscar Usuario\n
    - [3]buscar Usuario Especifico\n
    - [4]Atualiza Usuario\n
    - [5]Deleta Usuario\n
--------------------  [ Vendedor ]  --------------------  
    - [6]Criar Vendedor\n
    - [7]buscar Vendedor\n
    - [8]buscar Vendedor Especifico\n
    - [9]Atualiza Vendedor\n
    - [10]Deleta Vendedor\n
--------------------  [ Produto ]  --------------------  
    - [11]Criar Produto\n
    - [12]buscar Produto\n
    - [13]buscar Produto Especifico\n
    - [14]Atualiza Produto\n
    - [15]Deleta Produto\n
    ''')
        escolha = input(str('escolha Uma Obção:'))
        match escolha:
            case '0':
                app.close()
                print('Até mais...')
                execucao = False
            case '1':
                app.usuario()
            case '2':
                app.BuscarUsuarios()
            case '3':
                app.BuscarUsuarioCpf()
            case '4':
                app.AtualizarUsuario()
            case '5':
                app.deleteUsuario()
            case '6':
                app.CriarVendedor()
            case '7':
                app.BuscarVendedores()
            case '8':
                app.BuscarVendedorCnpj()
            case '9':
                app.AtualizarVendedor()
            case '10':
                app.deletarVendedor()
            case '11':
                app.CriarProduto()
            case '12':
                app.BuscarProdutos()
            case '13':
                app.BuscarProdutoEspecifico()
            case '14':
                app.AtualizarProduto()
            case '15':
                app.deletarProduto()