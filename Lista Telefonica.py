class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"O contato {nome} já existe na agenda.")
        else:
            self.contatos[nome] = telefone
            print(f"Contato {nome} adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado na agenda.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print(f"Contato {nome} não encontrado na agenda.")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            print("Lista de contatos:")
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")


def menu(agenda):
    while True:
        print("\n*** Menu da Agenda Telefônica ***")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Pesquisar contato")
        print("4. Listar contatos")
        print("5. Sair do programa")

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome do contato que deseja pesquisar: ")
            agenda.pesquisar_contato(nome)
        elif escolha == '4':
            agenda.listar_contatos()
        elif escolha == '5':
            print("Obrigado por usar a Agenda Telefônica. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")


if __name__ == "__main__":
    minha_agenda = AgendaTelefonica()
    menu(minha_agenda)
