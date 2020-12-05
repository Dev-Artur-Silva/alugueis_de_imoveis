import pandas as pd

class Proprietario:
    
    def __init__(self, nome, cpf, data):
        self.nome = nome 
        self.cpf = cpf
        self.data = data
    
    def cadastrar_proprietario(self, excel_proprietarios):
        linha = [self.nome, self.cpf, self.data]
        print(linha)
        excel_proprietarios.loc[len(excel_proprietarios)] = linha
    
    def relatorio_proprietarios(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data}')


class Imovel:

    def __init__(self, codigo, cpf, tipo, endereco, valor, status):
        self.codigo = codigo
        self.cpf = cpf
        self.tipo = tipo
        self.endereco = endereco
        self.valor = valor
        self.status = status
    
    def cadastrar_imovel(self, excel_imoveis):
        linha = [self.codigo, self.cpf, self.tipo, self.endereco, self.valor, self.status]
        excel_imoveis.loc[len(excel_imoveis)] = linha
    
    def relatorio_imoveis(self):
        pass

class Inquilino:

    def __init__(self, nome, cpf, data):
        self.nome = nome
        self.cpf = cpf
        self.data = data
    
    def cadastrar_inquilino(self, excel_inquilinos):
        linha = [self.nome, self.cpf, self.data]
        excel_inquilinos.loc[len(excel_inquilinos)] = linha
    
    def relatorio_inquilinos(self):
        pass

class Aluguel:

    def __init__(self, cpf, codigo, data_entrada):
        self.cpf = cpf
        self.codigo = codigo
        self.data_entrada = data_entrada
        self.data_saida = ''

    def registrar(self, excel_alugueis):
        linha = [self.cpf, self.codigo, self.data_entrada, self.data_saida]
        excel_alugueis.loc[len(excel_alugueis)] = linha
    
    def finalizar(self, data_saida):
        self.data_saida = data_saida
        pass
    
    def relatorio_alugueis(self):
        pass


def salvar_dados(excel_proprietarios, excel_imoveis, excel_inquilinos, excel_alugueis):
    # Criar objeto para leitura e selecionar planilha
    # Criar objeto para escrita
    excel_writer = pd.ExcelWriter("dados.xlsx")
    excel_proprietarios.to_excel(excel_writer, 'Proprietario', index=False)
    excel_imoveis.to_excel(excel_writer, 'Imovel', index=False)
    excel_inquilinos.to_excel(excel_writer, 'Inquilino', index=False)
    excel_alugueis.to_excel(excel_writer, 'Aluguel', index=False)
    # Salvar e fechar arquivo
    excel_writer.save()


def iniciar(lista_objetos, excel_proprietarios):
    for x, y in excel_proprietarios.iterrows():
        nome = y['Nome']
        cpf = y['CPF']
        data = y['Data de Nascimento']
        objeto = Proprietario(nome, cpf, data)
        lista_objetos.append(objeto)
        

def menu_um(excel_proprietarios, lista_objetos):

    while True:

        nome = input('Digite o nome do proprietario: ')

        while True:
            cpf = input('Digite o CPF do Proprietario (so numeros) ou 0 para sair: ')

            if cpf == '0':
                break

            elif len(cpf) != 11 or not cpf.isdigit():
                    print('E necessario 11 numeros.\n')
                    continue
            cpf = formatar_cpf(cpf)

            if verificar_cpf(cpf, lista_objetos):
                print('CPF ja cadastrado.')
                continue

            
            break
        
        if cpf == '0':
            break

        while True:

            data = input('Digite a data de nascimento (dd/mm/aaaa): ')

            if len(data) != 10:
                print('Digite no formato dd/mm/aaaa')
                continue
                
            elif data[2] != '/' or data[5] != '/':
                print('Digite no formato dd/mm/aaaa')
                continue

            break

        objeto = Proprietario(nome, cpf, data)
        objeto.cadastrar_proprietario(excel_proprietarios)
        lista_objetos.append(objeto)

        break
    

def formatar_cpf(cpf):
    cpf = (f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    return cpf

def verificar_cpf(cpf, lista_objetos):
    for x in lista_objetos:
        if x.cpf == cpf:
            return True
