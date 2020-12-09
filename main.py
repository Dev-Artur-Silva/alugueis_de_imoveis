import pandas as pd
import funcoes


objetos_proprietario = []
objetos_imovel = []
objetos_inquilino = []
objetos_aluguel = []

arquivo = pd.ExcelFile("C:dados.xlsx")
excel_proprietarios = pd.read_excel(arquivo, 'Proprietario')
excel_imoveis = pd.read_excel(arquivo, 'Imovel')
excel_inquilinos = pd.read_excel(arquivo, 'Inquilino')
excel_alugueis = pd.read_excel(arquivo, 'Aluguel')

funcoes.iniciar(objetos_proprietario, excel_proprietarios, excel_imoveis, objetos_imovel, objetos_inquilino, excel_inquilinos, objetos_aluguel, excel_alugueis)

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
            
            funcoes.menu_um(excel_proprietarios, objetos_proprietario, objetos_inquilino)
            funcoes.salvar_dados(excel_proprietarios, excel_imoveis, excel_inquilinos, excel_alugueis)

        elif (menu == 2):
            funcoes.menu_dois(excel_imoveis, objetos_proprietario, objetos_imovel, objetos_inquilino)
            funcoes.salvar_dados(excel_proprietarios, excel_imoveis, excel_inquilinos, excel_alugueis)
        elif (menu == 3):
            funcoes.menu_tres(excel_inquilinos, objetos_inquilino, objetos_proprietario)
            funcoes.salvar_dados(excel_proprietarios, excel_imoveis, excel_inquilinos, excel_alugueis)

        elif (menu == 4):
            funcoes.menu_quatro(objetos_inquilino, objetos_imovel, excel_alugueis, objetos_aluguel, excel_imoveis)
            funcoes.salvar_dados(excel_proprietarios, excel_imoveis, excel_inquilinos, excel_alugueis)

        elif (menu == 5):
            funcoes.menu_cinco(objetos_inquilino, objetos_aluguel, objetos_imovel, excel_imoveis, excel_alugueis)
            funcoes.salvar_dados(excel_proprietarios, excel_imoveis, excel_inquilinos, excel_alugueis)
        
        elif (menu == 6):
            funcoes.menu_seis(objetos_proprietario)

        elif (menu == 7):
            funcoes.menu_sete(objetos_imovel, objetos_proprietario)
                #Exibe todos os dados dos imóveis: Código, CPF e Nome do Proprietário, Tipo,
                #Endereço, Valor do Aluguel, Status Alugado;

        elif (menu == 8):
            funcoes.menu_oito(objetos_inquilino)

        elif (menu == 9):
            funcoes.menu_nove(objetos_aluguel, objetos_inquilino, objetos_proprietario, objetos_imovel)

            #Nome do Inquilino;
            #ii. Código, Tipo, Endereço e Nome Proprietário do imóvel;
            #iii. Valor do aluguel;
            #iv. Data início do aluguel;
            #v. Data fim do aluguel (se tiver finalizado);
        
        elif (menu == 10):
            funcoes.menu_dez(objetos_imovel, objetos_aluguel)
            #ALUGUEIS NAO FINALIZADOS!
            #valor cobrado para comissão pela imobiliária é de 10% do valor do aluguel.
            #i. Valor do aluguel;
            #ii. Data início do aluguel;
            #iii. Valor da comissão do imóvel;
            #iv. Valor Total da Comissão calculado desde a data do início do imóvel até a
            #data atual.
        elif (menu == 0):
            break

menu()