clientes = []

def mostrar_menu():
    print("\n--- MENU DE CLIENTES ---")
    print("1. Adicionar cliente")
    print("2. Listar clientes")
    print("3. Buscar cliente por nome")
    print("4. Remover cliente")
    print("5. Sair")
def adicionar_cliente():
    nome = input("Nome do cliente: ")
    cliente = {"nome": nome}
    clientes.append(cliente)
    print("Cliente adicionado com sucesso!")


def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- LISTA DE CLIENTES ---")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. Nome: {cliente['nome']}")

def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("\n--- LISTA DE CLIENTES ---")
    for i, cliente in enumerate(clientes, start=1):
        print(f"{i}. Nome: {cliente['nome']}")

def buscar_cliente():
    nome = input("Digite o nome do cliente que deseja buscar: ")
    encontrados = [c for c in clientes if nome.lower() in c['nome'].lower()]
    if encontrados:
        print("\n--- CLIENTES ENCONTRADOS ---")
        for cliente in encontrados:
            print(f"Nome: {cliente['nome']}")
    else:
        print("Nenhum cliente encontrado com esse nome.")

def remover_cliente():
    nome = input("Digite o nome do cliente que deseja remover: ")
    for cliente in clientes:
        if cliente["nome"].lower() == nome.lower():
            clientes.remove(cliente)
            print("Cliente removido com sucesso!")
            return
    print("Cliente não encontrado.")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        buscar_cliente()
    elif opcao == "4":
        remover_cliente()
    elif opcao == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
