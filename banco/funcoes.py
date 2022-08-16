import inquirer

#funcão de adicionar um novo usuário no arquivo txt usando nome e cpf
def add_user():
    while True:
        nome = input('Digite o nome completo: ').upper().strip()
        cpf = input('Digite seu CPF (XXX.XXX.XXX-XX): ')
        print('-'*60)
        print(f'NOME = {nome}\nCPF = {cpf}')
        confirmar = input('As informações estão corretas? [S/N] ').upper().strip()
        if confirmar == 'S':
            print('\33[32m~~~~~~~~~~~ CADASTRO EFETUADO COM SUCESSO ~~~~~~~~~~~\33[m')
            cadastros = open(r'usuarios.txt', 'a', encoding='utf-8')
            cadastros.write(f'{nome}_{cpf}\n')
            cadastros.close()
            break

#função de logar como adm validando o nome e cpf informados
def logar_adm():
    print('\33[30m\33[107m\33[1mOLÁ ADMINISTRADOR, CONFIRME SUA IDENTIDADE!\33[m')
    nome = input('Digite o nome completo: ').upper().strip()
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

#função de logar como um usuário já criado e fazer operações bancárias
def logar():
    nome = input('Digite o nome completo: ').upper().strip()
    cpf = input('Digite seu CPF (XXX.XXX.XXX-XX): ')
    #verifica se o nome e cpf estão cadastrados no arquivo usuários.txt, se não estiver vai pedir para cadastrar
    if nome and cpf in usuarios.txt:
        while True: 
            opcoes = [
                inquirer.List(
                    'escolha',
                    message = 'Opções do Banco:',
                    choices = ['Fazer Transações', 'Consultar saldo', 'Sacar dinheiro', 'Depositar dinheiro']
                )
            ]
            respostas = inquirer.prompt(opcoes)

            if respostas['escolha'] == 'Fazer Transações':
                    transacoes()
    else:
        print('O usuário acima não existe!')

#função de sair do banco
def sair():
    print('\33[36m\33[4m>>>>>   Até a próxima DEV <3\33[m')


#OPÇÕES DO USUÁRIO
def transacoes():
    while True:
        pessoas = [
            inquirer.List(
                'escolha',
                message = 'Pessoas cadastradas no Banco',
                choices = ['']
            )
        ]
        respostas = inquirer.prompt(pessoas)

        if respostas['escolha'] == 'usuarios.txt':
            pass