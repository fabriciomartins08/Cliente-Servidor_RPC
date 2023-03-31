import xmlrpc.client

# Conecta ao servidor
server = xmlrpc.client.ServerProxy('http://localhost:8000')

# Menu interativo
while True:
    print("=== MENU ===")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Procurar por letra")
    print("4 - Procurar por nome")
    print("5 - Pegar próximo contato")
    print("6 - Pegar próxima letra")
    print("7 - Pegar contato pelo ID")
    print("8 - Listar todos os contatos")
    print("0 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        client_id = input("Digite o ID do cliente: ")
        name = input("Digite o nome do contato: ")
        phone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        server.adicionar_contato(int(client_id), name, phone, email)
        print("Contato adicionado com sucesso!")

    elif escolha == '2':
        client_id = input("Digite o ID do cliente: ")
        contact_id = input("Digite o ID do contato: ")
        server.remover_contato(int(client_id), int(contact_id))
        print("Contato removido com sucesso!")

    elif escolha == '3':
        client_id = input("Digite o ID do cliente: ")
        letter = input("Digite a letra inicial do nome: ")
        contatos = server.procurar_por_letra(int(client_id), letter)
        print("Contatos encontrados:")
        for contato in contatos:
            print(contato)

    elif escolha == '4':
        client_id = input("Digite o ID do cliente: ")
        name = input("Digite o nome do contato: ")
        contatos = server.procurar_por_nome(int(client_id), name)
        print("Contatos encontrados:")
        for contato in contatos:
            print(contato)

    elif escolha == '5':
        client_id = input("Digite o ID do cliente: ")
        contato = server.pegue_proximo_contato(int(client_id))
        print("Próximo contato:")
        print(contato)

    elif escolha == '6':
        client_id = input("Digite o ID do cliente: ")
        letter = input("Digite a letra inicial: ")
        proxima_letra = server.pegue_proxima_letra(int(client_id), letter)
        if proxima_letra is not None:
            print("Próxima letra:", proxima_letra)
        else:
            print("Não há mais letras disponíveis.")

    elif escolha == '7':
        client_id = input("Digite o ID do cliente: ")
        contact_id = input("Digite o ID do contato: ")
        contato_index = server.pegue_contato_index_do_id(int(client_id), int(contact_id))
        if contato_index is not None:
            print("Índice do contato:", contato_index)
        else:
            print("Contato não encontrado.")

    elif escolha == '8':
        contatos = server.carregar_contatos()
        print("Contatos cadastrados:")
        for contato in contatos:
            print(contato)

    elif escolha == '0':
        break

    else:
        print("Opção inválida!")
