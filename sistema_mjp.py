import mysql.connector
from datetime import datetime
from time import sleep

conexao = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'minha_senha_aqui',
    database= 'cadastro',
)

cursor = conexao.cursor()


#CREATE
def criar_manifesto():
    manifesto = input("Manifesto: ")
    cte = input("CTE: ")
    data = datetime.now().strftime("%Y/%m/%d")
    comando = f"INSERT INTO manifestos(numero_manifesto, numero_cte, data_registro) VALUES('{manifesto}', '{cte}', '{data}')"
    print('Manifesto registrado com sucesso!')
    cursor.execute(comando)
    conexao.commit()
#READ
def listar_manifesto():
    comando = f"SELECT * FROM manifestos"
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print('-----------------------------------')
    print(f"{"ID | CTE | MANIFESTO | DATA".center(35)}")
    print('-----------------------------------')
    for linha in resultado:
        print(f' {linha[0]} | {linha[1]} -> {linha[2]} | \033[35m{linha[3]}\033[m')

#UPDATE
def atualizar_manifesto():
    comando = None
    id_manifesto = input("Digite o ID do manifesto que você deseja atualizar: ")
    print('----O que você deseja atualizar?----')
    print('1. Número do Manifesto')
    print('2. Número do CTE')
    print('3. Tudo')
    print('4. Sair')
    try:
        opcao = input('Escolha uma das opções: ')
        if opcao == '1':
            novo_manifesto = input("Novo número do Manifesto: ")
            comando = f"UPDATE manifestos SET numero_manifesto = '{novo_manifesto}' WHERE id = {id_manifesto}"
            print(f'Manifesto {novo_manifesto} atualizado com sucesso!')
        elif opcao == '2':
            novo_cte = input("Novo CTE: ")
            comando = f"UPDATE manifestos SET numero_cte = '{novo_cte}' WHERE id = {id_manifesto}"
            print(f'CTE {novo_cte} atualizado com sucesso!')
        elif opcao == '3':
            m = input("Novo Manifesto: ")
            c = input("Novo CTE: ")
            comando = f"UPDATE manifestos SET numero_manifesto = '{m}' , numero_cte = '{c}' WHERE id = {id_manifesto} "
            print(f'Manifesto {m} e CTE {c} atualizado com sucesso!')
        elif opcao == '4':
            print("Saindo...")
            return
        else:
            print('\033[31mOPÇÃO INVÁLIDA! Tente novamente.\033[m')
            return
        if comando:
            cursor.execute(comando)
            conexao.commit()

    except Exception as e:
        print(f'Ocorreu um erro: {e}')


#DELETE
def deletar_manifesto():
    print('-----DELETAR MANIFESTOS-----')
    print(' 1.Deletar pelo ID')
    print(' 2.Deletar Todos')
    comando = None
    opc = int(input('Escolha: '))
    if opc == 1:
        id_manifesto = input("Digite o ID do Manifesto: ")
        comando = f"DELETE FROM manifestos WHERE id = {id_manifesto}"
        print(f'Manifesto {id_manifesto} deletado com sucesso!')
    elif opc == 2:
        resp = str(input('Tem certeza que deseja excluir todos os manifestos? [S/N]: ')).strip().upper()[0]
        if resp == 'S':
            comando = f"TRUNCATE TABLE manifestos"
            print('Todos os manifestos foram deletados com sucesso!')
        elif resp == 'N':
             print('Saindo...')
             return
    if comando:
        cursor.execute(comando)
        conexao.commit()

#MENU PRINCIPAL
def menu():
    while True:
        try:
            sleep(0.5)
            print('\033[36m-' * 30)
            print(f'{"MJP TRANSPORTES".center(30)}')
            print('-' * 30)
            sleep(0.5)
            print('O que você deseja fazer?')
            print('1. Criar Manifestos')
            print('2. Consultar Manifestos')
            print('3. Atualizar Manifestos')
            print('4. Deletar Manifestos')
            print('5. Sair do Programa\033[m')
            opcao = int(input('Escolha sua opção: '))
            if opcao == 1:
                criar_manifesto()
            elif opcao == 2:
                listar_manifesto()
            elif opcao == 3:
                atualizar_manifesto()
            elif opcao == 4:
                deletar_manifesto()
            elif opcao == 5:
                print('Encerrando o programa...')
                cursor.close()
                conexao.close()
                sleep(1)
                break
            else:
                print('\033[31mOPÇÃO INVÁLIDA! Tente novamente.\033[m')
        except Exception as e:
            print(f'\033[31mOcorreu um erro: {e}\033[m')
menu()
