from ast import Continue
import inquirer

def menu():
    while True: 
        perguntas = [
            inquirer.List(
                'escolha',
                message = 'MENU',
                choices = ['Adicionar novo usuário', 'Logar como Administrador', 'Logar como usuário', 'Sair do banco']
            )
        ]

        print('='*50)
        print(' -=-=-=-=-=-=-=-=- BANCO DA TAY -=-=-=-=-=-=-=-=-')
        print('='*50)
        respostas = inquirer.prompt(perguntas)

        if respostas['escolha'] == 'Adicionar novo usuário':
            add_user()

        elif respostas['escolha'] == 'Logar como Administrador':
            logar_adm()

        elif respostas['escolha'] == 'Logar como usuário':
            logar()

        elif respostas['escolha'] == 'Sair do banco':
            sair()
            break

def options_bank():
    while True: 
                opcoes = [
                    inquirer.List(
                        'escolha',
                        message = 'OPÇÕES DO BANCO',
                        choices = ['Fazer Transações', 'Consultar saldo', 'Sacar dinheiro', 'Depositar dinheiro']
                    )
                ]
                respostas = inquirer.prompt(opcoes)

                if respostas['escolha'] == 'Fazer Transações':
                    transacoes()
                elif respostas['escolha'] == 'Consultar saldo':
                    saldo()
                elif respostas['escolha'] == 'Sacar dinheiro':
                    saque()
                elif respostas['escolha'] == 'Depositar dinheiro':
                    deposito()
                break


#funcão de adicionar um novo usuário no arquivo txt usando nome e cpf
def add_user():
    while True:
        nome = input('Digite seu nome completo: ').upper().strip()
        cpf = input('Digite seu CPF (XXX.XXX.XXX-XX): ')
        print('-'*50)
        print(f'NOME = {nome}\nCPF = {cpf}')
        users = open(r'usuarios.txt', 'r', encoding='utf-8')
        cadastros = users.readlines()
        usuario_existe = False

        for cadastro in cadastros:
            separando = cadastro.split('_')

            if separando[1].strip() == cpf:
                print('CPF já cadastrado')
                usuario_existe = True

        if usuario_existe:
            continue

        else:
            confirmar = input('As informações estão corretas? [S/N] ').upper().strip()
            if confirmar == 'S':
                print('Por ser um novo usuário R$500,00 foram adicionados a sua conta! APROVEITE :)')
                print('\33[32m~~~~~~~~~~~ CADASTRADO(A) COM SUCESSO ~~~~~~~~~~~\33[m')
                cadastros = open(r'usuarios.txt', 'a', encoding='utf-8')
                cadastros.write(f'{nome}_{cpf}_500\n')
                cadastros.close()
                break
        menu()

#função de logar como adm validando o nome e cpf informados
def logar_adm():
    print('\33[30m\33[107m\33[1mOLÁ ADMINISTRADOR, CONFIRME SUA IDENTIDADE!\33[m')
    nome = input('Digite seu nome completo: ').upper().strip()
    cpf = input('Digite seu CPF (XXX.XXX.XXX-XX): ')
    adm = open(r'adm.txt', 'r', encoding='utf-8')
    admin = adm.read().split('_')
    if admin[0] == nome:
        if admin[1] == cpf:
            print('\033[1;35m>>>>>   BEM-VINDA ADM\033[0;0m')
        else:
            print('\033[1;31mCPF INCORRETO, TENTE NOVAMENTE MAIS TARDE!\033[0;0m')
    else:
        print('\033[1;31mNOME INCORRETO, TENTE NOVAMENTE MAIS TARDE!\033[0;0m')

    menu()

#função de logar como um usuário já criado e fazer operações bancárias
def logar():
    nome = input('Digite seu nome completo: ').upper().strip()
    cpf = input('Digite seu CPF (XXX.XXX.XXX-XX): ')

    #verifica se o nome e cpf estão cadastrados no arquivo usuários.txt, se não estiver vai pedir para cadastrar
    users = open(r'usuarios.txt', 'r', encoding='utf-8')
    cadastros = users.readlines()

    confirmar = input('As informações estão corretas? [S/N] ').upper().strip()
    if confirmar == 'S':
        for index, cadastro in enumerate(cadastros):
            separando = cadastro.split('_')
            if separando[0] == nome and separando[1].strip() == cpf:
                print('\33[32m~~~~~~ USUÁRIO LOGADO COM SUCESSO ~~~~~~\33[m')
                print('*'*40)
                options_bank()
                    
        else:
            print('\033[1;31m~~~~~~~~~~ O usuário acima não existe! ~~~~~~~~~~~\033[0;0m')
            menu()
    else:
        logar()


#função de sair do banco
def sair():
    print('\33[36m\33[4m>>>>>   Até a próxima DEV <3\33[m')


#--------------- OPÇÕES DO USUÁRIO --------------------------------------------
def transacoes():
    users = open(r'usuarios.txt', 'r', encoding='utf-8')
    cadastros = users.readlines()

    lista_nomes = []
    
    for cadastro in cadastros:
        lista_nomes.append(cadastro.split('_')[0])

    while True:
        pessoas = [
            inquirer.List(
                'escolha',
                message = 'Pessoas cadastradas no Banco',
                choices = lista_nomes
            )
        ]
        respostas = inquirer.prompt(pessoas)

        if respostas['escolha'] == 'usuarios.txt':
            pass

            menu()


def saque():
    print('''CÉDULAS DISPONÍVEIS: 
    >>>>>>  R$ 1,00
    >>>>>>  R$ 5,00
    >>>>>>  R$10,00
    >>>>>>  R$20,00
    >>>>>>  R$50,00
    >>>>>> R$100,00
''')

    saque = int(input('Qual o valor a ser sacado? R$'))

    cem = cinq = vinte = dez = cinco = um = 0
    while True:
        while saque - 100 >= 0:
            saque -= 100
            cem += 1
        while saque - 50 >= 0:
            saque -= 50
            cinq += 1
        while saque - 20 >= 0:
            saque -= 20
            vinte += 1
        while saque - 10 >= 0:
            saque -= 10
            dez += 1
        while saque - 5 >= 0:
            saque -= 5
            cinco += 1
        while saque - 1 >= 0:
            saque -= 1
            um += 1
        break

    if cem != 0:
        print(f'Total de {cem} cédula(s) de R$100')
    if cinq != 0:
        print(f'Total de {cinq} cédula(s) de R$50')
    if vinte != 0:
        print(f'Total de {vinte} cédula(s) de R$20')
    if dez != 0:
        print(f'Total de {dez} cédula(s) de R$10')
    if cinco != 0:
        print(f'Total de {cinco} cédula(s) de R$5')
    if um != 0:
        print(f'Total de {um} cédula(s) de R$1')
    
    options_bank()

# verificar saldo da sua conta
def saldo():
    users = open(r'usuarios.txt', 'r', encoding='utf-8')
    cadastros = users.readlines()

    for cadastro in cadastros:
        saldo = cadastro.split('_')[2].strip()
    print(f'Você tem R${saldo},00 na conta!')
    options_bank()


# fazer depósito para a sua conta
def deposito():
    depositar = int(input('Digite o valor que deseja depositar na sua conta: R$'))

    users = open(r'usuarios.txt', 'r', encoding='utf-8')
    cadastros = users.readlines()

    
    print(f'{depositar:.2f}').replace('.', ',')
