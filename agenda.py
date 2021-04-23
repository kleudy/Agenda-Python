def menu():
    voltarMenu = 's'
    while voltarMenu == 's':
        opcao = input('''
        =========================================
                PROJETO AGENDA EM PYTHON
        MENU:
        [1] CADASTRAR
        [2] LISTAR CONTATO
        [3] DELETAR CONTATO
        [4] BUSCAR CONTATO PELO ID
        [5] SAIR
        =========================================
        ESCOLHA UMA OPÇÃO ACIMA: 
        ''')
        if opcao == '1':
            cadastrarContato()
        elif opcao == '2':
            listarContato()
        elif opcao == '3':
            deletarContato()
        elif opcao == '4':
            bascarContatoPeloId()
        else:
            sair()
        voltarMenu = input(
            'Deseja voltar para o Menu principal? (s/n) ').lower()


def cadastrarContato():
    idContato = input('Informe o Id do contato: ')
    nome = input(f'Informe o nome do contato para o id {idContato}: ')
    telefone = input(f'Informe o telefone do {nome}: ')
    email = input(f'Informe o E-mail do {nome}: ')
    try:
        agenda = open('agenda.txt', 'a')
        dados = f'{idContato};{nome};{telefone};{email}\n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!')
    except:
        print(f'Erro na gravação do contato {nome}')


def listarContato():
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        print(contato)


def deletarContato():
    aux = []
    aux2 = []
    nomeDeletado = input('Informe o nome para ser deletado: ').upper()
    try:
        agenda = open('agenda.txt', 'r')
        for linha in agenda:
            aux.append(linha)
        for i in range(0, len(aux)):
            if nomeDeletado not in aux[i].upper():
                aux2.append(aux[i])
        agenda.close()
        agenda = open('agenda.txt', 'w')
        for i in aux2:
            agenda.write(i)
        agenda.close()
        print(f'{nomeDeletado} foi feletado da base!')
        listarContato()
    except:
        print(f'Erro ao tentar deletar {nomeDeletado} da base')


def bascarContatoPeloId():
    nome = input('Informe o nome a ser pesquisado: ').upper()
    agenda = open('agenda.txt', 'r')
    for contato in agenda:
        if nome in contato.split(';')[1].upper():
            print(contato)


def sair():
    print('Fechando o programa.')
    exit()


def main():
    menu()


main()
