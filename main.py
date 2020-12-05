import pandas as pd
import funcoes


lista_objetos = []



arquivo = pd.ExcelFile("C:dados.xlsx")
excel_proprietarios = pd.read_excel(arquivo, 'Proprietario')
excel_imoveis = pd.read_excel(arquivo, 'Imovel')
excel_inquilinos = pd.read_excel(arquivo, 'Inquilino')
excel_alugueis = pd.read_excel(arquivo, 'Aluguel')

funcoes.iniciar(lista_objetos, excel_proprietarios)

def menu():

    while True:
        print('''
        Escolha uma opção do menu:
        1 - Cadastrar Proprietario
        2 - Cadastrar Imovel
        3 - Cadastrar Inquilino
        4 - Registrar Aluguel
        5 - Finalizar Aluguel
        6 - Relatorio de Proprietarios
        7 - Relatorio de Imoveis
        8 - Relatorio de Inquilinos
        9 - Relatorio de Alugueis
        10 - Relatorio de Comissoes
        0 - Sair
        ''')

        try:
            menu = int(input('O que deseja? '))
            print()
            assert 0 <= menu <= 10
        except AssertionError:
            print('Valor fora do limite.')
            continue
        except ValueError:
            print('Somente numeros.')
            continue
        
        if (menu == 1):
            
            funcoes.menu_um(excel_proprietarios, lista_objetos)
            funcoes.salvar_dados(excel_proprietarios, excel_imoveis, excel_inquilinos, excel_alugueis)

        elif (menu == 2):
            pass

        elif (menu == 3):
            pass

        elif (menu == 4):
            pass

        elif (menu == 5):
            pass
        
        elif (menu == 6):
            for x in lista_objetos:
                x.relatorio_proprietarios()

        elif (menu == 7):
            pass

        elif (menu == 8):
            pass

        elif (menu == 9):
            pass
            
        elif (menu == 0):
            break

menu()