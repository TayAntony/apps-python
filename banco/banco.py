import inquirer
from funcoes import *

while True: 
    perguntas = [
        inquirer.List(
            'escolha',
            message = 'MENU',
            choices = ['Adicionar novo usuário', 'Logar como Administrador', 'Logar como usuário', 'Sair do banco']
        )
    ]
    print('='*32)
    print('-=-=-=-=- BANCO DA TAY -=-=-=-=-')
    print('='*32)
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
