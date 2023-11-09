# melhorar cliente, usar Connector
class Cliente:
    def __init__(self, nome, sobrenome, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email

class SistemaCadastroClientes:
    def __init__(self):
        self.clientes = []

    def inserir_cliente(self, nome, sobrenome, email):
        cliente = Cliente(nome, sobrenome, email)
        self.clientes.append(cliente)
        print(f"Cliente {nome} {sobrenome} inserido com sucesso.")

    def listar_clientes(self):
        if self.clientes:
            print("Lista de clientes:")
            for i, cliente in enumerate(self.clientes, 1):
                print(f"{i}. {cliente.nome} {cliente.sobrenome} - {cliente.email}")
        else:
            print("Nenhum cliente cadastrado.")

    def consultar_cliente(self, email):
        for cliente in self.clientes:
            if cliente.email == email:
                print(f"Cliente encontrado: {cliente.nome} {cliente.sobrenome} - {cliente.email}")
                return cliente
        print("Cliente não encontrado.")
        return None

    def alterar_cliente(self, email, novo_nome, novo_sobrenome, novo_email):
        cliente = self.consultar_cliente(email)
        if cliente:
            cliente.nome = novo_nome
            cliente.sobrenome = novo_sobrenome
            cliente.email = novo_email
            print("Cliente alterado com sucesso.")

    def remover_cliente(self, email):
        cliente = self.consultar_cliente(email)
        if cliente:
            self.clientes.remove(cliente)
            print("Cliente removido com sucesso.")


sistema = SistemaCadastroClientes()


sistema.inserir_cliente("Matteo", "Kurpjuweit", "matteo@email.com")
sistema.inserir_cliente("Ana", "Maiello", "ana@email.com")


sistema.listar_clientes()

# consulta
sistema.consultar_cliente("matteo@email.com")
sistema.alterar_cliente("matteo@email.com", "Matteo", "Fischer", "matteo.fischer@email.com")

# remover 
sistema.remover_cliente("ana@email.com")

# lista
sistema.listar_clientes()


