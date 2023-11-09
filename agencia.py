# melhorar agencia, tirar o cadastro para usar Connector
class Agencia:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def __str__(self):
        return f"Agência: {self._nome}, Endereço: {self._endereco}"

    def get_nome(self):
        return self._nome

    def get_endereco(self):
        return self._endereco

    def descricao(self):
        return "Agência Genérica"

class AgenciaPrincipal(Agencia):
    def descricao(self):
        return f"{self.get_nome()} - Agência Principal"

class AgenciaSecundaria(Agencia):
    def descricao(self):
        return f"{self.get_nome()} - Agência Secundária"

class CadastroAgencias:
    def __init__(self):
        self.agencias = []

    def inserir_agencia(self, agencia):
        if isinstance(agencia, Agencia):
            self.agencias.append(agencia)
            print(f"{agencia.descricao()} inserida com sucesso.")
        else:
            print("Erro: O objeto não é do tipo Agência.")

    def listar_agencias(self):
        if self.agencias:
            print("Lista de agências:")
            for agencia in self.agencias:
                print(agencia)
        else:
            print("Nenhuma agência cadastrada.")


cadastro_agencias = CadastroAgencias()

# agencias diferentes
agencia_principal = AgenciaPrincipal("Agência Central", "Rua Antonio Andrade, 123")
agencia_secundaria = AgenciaSecundaria("Agência Filial", "Rua Bernardo Ferraz de Almeida, 232")

# colocando agencias no cadastro
cadastro_agencias.inserir_agencia(agencia_principal)
cadastro_agencias.inserir_agencia(agencia_secundaria)

# list agencias
cadastro_agencias.listar_agencias()


