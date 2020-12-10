import pandas as pd
from datetime import *

class Proprietario:
    
    def __init__(self, nome, cpf, data):
        self.nome = nome
        self.cpf = cpf
        self.data = data

    def cadastrar_proprietario(self, excel_proprietarios):
        linha = [self.nome, self.cpf, self.data]
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
    
    def relatorio_imoveis(self, nome):
        print(f'''Codigo: {self.codigo}, CPF: {self.cpf}, Nome do Proprietario: {nome}, Tipo: {self.tipo}, Endereco: {self.endereco},
Valor do aluguel: {self.valor}, Aluguel Cadastrado: {self.status}\n''')

class Inquilino:

    def __init__(self, nome, cpf, data):
        self.nome = nome
        self.cpf = cpf
        self.data = data
    
    def cadastrar_inquilino(self, excel_inquilinos):
        linha = [self.nome, self.cpf, self.data]
        excel_inquilinos.loc[len(excel_inquilinos)] = linha
    
    def relatorio_inquilinos(self):
        print(f'Nome: {self.nome}, CPF: {self.cpf}, Data de Nascimento: {self.data}')

class Aluguel:

    def __init__(self, cpf, codigo, data_entrada, data_saida):
        self.cpf = cpf
        self.codigo = codigo
        self.data_entrada = data_entrada
        self.data_saida = data_saida

    def registrar(self, excel_alugueis):
        linha = [self.cpf, self.codigo, self.data_entrada, self.data_saida]
        excel_alugueis.loc[len(excel_alugueis)] = linha
    
    def finalizar(self, data_saida, posicao, excel_alugueis):
        self.data_saida = data_saida
        excel_alugueis.loc[posicao, 'Data de Saida'] = self.data_saida

    def relatorio_alugueis(self, nome_inquilino, codigo, tipo, endereco, nome_proprietario, valor, data_entrada, data_saida):
        print(f'''
        Nome do inquilino: {nome_inquilino}.
        Codigo: {codigo}, Tipo: {tipo}, Endereco: {endereco}, Nome do Proprietario: {nome_proprietario}
        Valor do Aluguel: {valor}
        Data de entrada: {data_entrada}
        Data de Saida: {data_saida}
        ''')

class Comissoes:
    def __init__(self, valor, data_entrada, comissao, total):
        self.valor = valor 
        self.data_entrada = data_entrada
        self.comissao = comissao
        self.total = total

    def relatorio_comissoes(self):
        print(f'Valor: {self.valor}, Data de Entrada: {self.data_entrada}, Valor da comissao: {self.comissao}, Total da comissao: {self.total}')

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


def iniciar(objetos_proprietario, excel_proprietarios, excel_imoveis, objetos_imovel, objetos_inquilino, excel_inquilinos, objetos_aluguel, excel_alugueis):
    for x, y in excel_proprietarios.iterrows():
        nome = y['Nome']
        cpf = y['CPF']
        data = y['Data de Nascimento']
        objeto = Proprietario(nome, cpf, data)
        objetos_proprietario.append(objeto)
        
    for x, y in excel_imoveis.iterrows():
        codigo = y['Codigo']
        cpf = y['CPF do Proprietario']
        tipo = y['Tipo']
        endereco = y['Endereco']
        valor = y['Valor']
        status = y['Status']
        objeto = Imovel(codigo, cpf, tipo, endereco, valor, status)
        objetos_imovel.append(objeto)
    
    for x, y in excel_inquilinos.iterrows():
        nome = y['Nome']
        cpf = y['CPF']
        data = y['Data de Nascimento']
        objeto = Inquilino(nome, cpf, data)
        objetos_inquilino.append(objeto)

    for x, y in excel_alugueis.iterrows():
        cpf = y['CPF do Inquilino']
        codigo = y['Codigo do Imovel']
        data_entrada = y['Data de Entrada']
        data_saida = y['Data de Saida']
        objeto = Aluguel(cpf, codigo, data_entrada, data_saida)
        objetos_aluguel.append(objeto)

def menu_um(excel_proprietarios, objetos_proprietario, objetos_inquilino):

    while True:

        nome = input('Digite o nome do Proprietario: ').capitalize()

        while True:
            cpf = input('Digite o CPF do Proprietario (so numeros) ou 0 para sair: ')

            if cpf == '0':
                break

            elif len(cpf) != 11 or not cpf.isdigit():
                    print('E necessario 11 numeros.\n')
                    continue
            cpf = formatar_cpf(cpf)

            if verificar_cpf_proprietario(cpf, objetos_proprietario) or cadastro_cpf_inquilino(cpf, objetos_inquilino):
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
        objetos_proprietario.append(objeto)
        print('Cadastro efetuado!')
        break
    
def menu_dois(excel_imoveis, objetos_proprietario, objetos_imovel, objetos_inquilino):
    while True:    
            
        try:
            codigo = int(input('Digite o codigo do imovel(0 para sair): '))

            if codigo == 0:
                break

            elif verificar_imovel(codigo, objetos_imovel):
                print('Codigo de imovel ja cadastrado.')
                continue
            
            while True:

                cpf = input('Digite o CPF do Proprietario (so numeros) ou 0 para sair: ')

                if cpf == '0':
                    break

                elif len(cpf) != 11 or not cpf.isdigit():
                        print('E necessario 11 numeros.\n')
                        continue

                cpf = formatar_cpf(cpf)

                if cadastro_cpf_inquilino(cpf, objetos_inquilino):
                    print('Informe um CPF de Proprietario.')
                    continue

                elif not verificar_cpf_proprietario(cpf, objetos_proprietario):
                    print('Proprietario nao cadastrado.')
                    continue
            
                break
        
            if cpf == '0':
                break
            
            while True:    
                tipo = str(input('Tipo da casa(Casa ou Apartamento): ')).capitalize()

                if tipo == 'Casa' or tipo == 'Apartamento':
                    break
            
            endereco = input('Informe o endereco do Imovel: ').capitalize()
            
            while True:    
                try:
                    valor = float(input('Valor do aluguel: '))
                    break
                except ValueError:
                    print('Apenas numeros')
            
            print('Imovel alugado: Nao')
            status = 'Nao'
            objeto = Imovel(codigo, cpf, tipo, endereco, valor, status)
            objeto.cadastrar_imovel(excel_imoveis)
            objetos_imovel.append(objeto)
            print('Cadastro efetuado!')
            break

        except ValueError:
            print('Apenas numeros.')
            
def menu_tres(excel_inquilinos, objetos_inquilino, objetos_proprietario):
   while True:

        nome = input('Digite o nome do Inquilino: ').capitalize()

        while True:
            cpf = input('Digite o CPF do Inquilino (so numeros) ou 0 para sair: ')

            if cpf == '0':
                break

            elif len(cpf) != 11 or not cpf.isdigit():
                    print('E necessario 11 numeros.\n')
                    continue
            cpf = formatar_cpf(cpf)

            if verificar_cpf_proprietario(cpf, objetos_proprietario) or cadastro_cpf_inquilino(cpf, objetos_inquilino):
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

        objeto = Inquilino(nome, cpf, data)
        objeto.cadastrar_inquilino(excel_inquilinos)
        objetos_inquilino.append(objeto)
        print('Cadastro efetuado!')
        break 

def menu_quatro(objetos_inquilino, objetos_imovel, excel_alugueis, objetos_aluguel, excel_imoveis):
    while True:
        cpf = input('Digite o CPF do Inquilino (so numeros) ou 0 para sair: ')

        if cpf == '0':
            break

        elif len(cpf) != 11 or not cpf.isdigit():
            print('E necessario 11 numeros.\n')
            continue

        cpf = formatar_cpf(cpf)

        if not cadastro_cpf_inquilino(cpf, objetos_inquilino):
            print('Inquilino nao cadastrado.')
            continue

        elif verificar_cpf_aluguel(cpf, objetos_aluguel, objetos_imovel):
            print('Ja ha um aluguel com esse CPF')
            continue
        
        while True:
            try:
                codigo = int(input('Digite o codigo do imovel(0 para sair): '))
                    
                if codigo == 0:
                    break
                
                elif not verificar_imovel(codigo, objetos_imovel):
                    print('Imovel nao cadastrado.')
                    continue
                
                elif verificar_aluguel_cadastrado(codigo, excel_alugueis, excel_imoveis):
                    print('Imovel ja alugado.')
                    continue
                
                elif verificar_aluguel_inquilino(codigo, cpf, objetos_aluguel):
                    print('Esse inquilino ja foi cadastrado neste imovel. ')
                    continue
                
                break
            except ValueError:
                print('somente numeros')

        if codigo == 0:
            break

        while True:
            data_entrada = input('Digite a data de entrada (dd/mm/aaaa): ')

            if len(data_entrada) != 10:
                print('Digite no formato dd/mm/aaaa')
                continue
                    
            elif data_entrada[2] != '/' or data_entrada[5] != '/':
                print('Digite no formato dd/mm/aaaa')
                continue
            
            break

        data_saida = 'ainda alugado'
        mudar_status_sim(codigo, objetos_imovel, excel_imoveis)
        objeto = Aluguel(cpf, codigo, data_entrada, data_saida)
        objeto.registrar(excel_alugueis)
        objetos_aluguel.append(objeto)
        print('Aluguel efetuado!')
        break


def menu_cinco(objetos_inquilino, objetos_aluguel, objetos_imovel, excel_imoveis, excel_alugueis):
    while True:
        cpf = input('Digite o CPF do Inquilino (so numeros) ou 0 para sair: ')

        if cpf == '0':
            break

        elif len(cpf) != 11 or not cpf.isdigit():
            print('E necessario 11 numeros.\n')
            continue

        cpf = formatar_cpf(cpf)

        if not cadastro_cpf_inquilino(cpf, objetos_inquilino):
            print('Inquilino nao cadastrado.')
            continue

        elif not verificar_cpf_aluguel(cpf, objetos_aluguel, objetos_imovel):
            print('Inquilino nao tem aluguel.')
            continue
        
        while True:
            try:
                codigo = int(input('Digite o codigo do imovel(0 para sair): '))
                    
                if codigo == 0:
                    break
                
                elif not verificar_imovel(codigo, objetos_imovel):
                    print('Imovel nao cadastrado.')
                    continue
                
                elif not verificar_alugado(codigo, objetos_aluguel, objetos_imovel):
                    print('Imovel nao alugado.')
                    continue
                
                break
            except ValueError:
                print('Somente numeros')
        
        data_saida = datetime.today().strftime('%Y-%m-%d')

        objeto = pegar_objeto_finalizar(cpf, codigo, objetos_aluguel)
        posicao = posicao_aluguel_dataframe(cpf, codigo, excel_alugueis)
        objeto.finalizar(data_saida, posicao, excel_alugueis)
        mudar_status_nao(codigo, objetos_imovel, excel_imoveis)
        print('Aluguel finalizado!')
        break

def menu_seis(objetos_proprietario):
    for x in objetos_proprietario:
        x.relatorio_proprietarios()

def menu_sete(objetos_imovel, objetos_proprietario):
    for x in objetos_imovel:
        for y in objetos_proprietario:
            if x.cpf == y.cpf:
                x.relatorio_imoveis(y.nome)

def menu_oito(objetos_inquilino):
    for x in objetos_inquilino:
        x.relatorio_inquilinos()

def menu_nove(objetos_aluguel, objetos_inquilino, objetos_proprietario, objetos_imovel):
    for a in objetos_aluguel:

        for i in objetos_inquilino:

            for p in objetos_proprietario:

                for m in objetos_imovel:

                    if a.cpf == i.cpf:
                        nome_inquilino = i.nome
                        if p.cpf == m.cpf:
                            codigo = m.codigo
                            tipo = m.tipo
                            endereco = m.endereco
                            nome_proprietario = p.nome
                            if m.codigo == a.codigo:
                                valor = m.valor
                                data_entrada = a.data_entrada
                                data_saida = a.data_saida
                                a.relatorio_alugueis(nome_inquilino, codigo, tipo, endereco, nome_proprietario, valor, data_entrada, data_saida)
                                        

def menu_dez(objetos_imovel, objetos_aluguel):
    for m in objetos_imovel:
        if m.status == 'Sim':
            for y in objetos_aluguel:
                if y.data_saida[4] != '-' and m.codigo == y.codigo:
                    meses = pegar_meses(y.data_entrada)
                    total = (m.valor * (10/100)) * meses
                    comissoes = Comissoes(m.valor, y.data_entrada, (m.valor*(10/100)), total)
                    comissoes.relatorio_comissoes()
                    
                    



def formatar_cpf(cpf):
    cpf = (f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
    return cpf

def verificar_cpf_proprietario(cpf, objetos_proprietario):
    for x in objetos_proprietario:
        if x.cpf == cpf:
            return True

def cadastro_cpf_inquilino(cpf, objetos_inquilino):
    for x in objetos_inquilino:
        if x.cpf == cpf:
            return True

def verificar_imovel(codigo, objetos_imovel):
    for x in objetos_imovel:
        if x.codigo == codigo:
            return True

def mudar_status_sim(codigo, objetos_imovel, excel_imoveis):
    for x in objetos_imovel:
        if codigo == x.codigo:
            x.status = 'Sim'
    
    for x, y in excel_imoveis.iterrows():
        if codigo == y['Codigo']:
            excel_imoveis.loc[x, 'Status'] = 'Sim'

def mudar_status_nao(codigo, objetos_imovel, excel_imoveis):
    for x in objetos_imovel:
        if codigo == x.codigo:
            x.status = 'Nao'
    
    for x, y in excel_imoveis.iterrows():
        if codigo == y['Codigo']:
            excel_imoveis.loc[x, 'Status'] = 'Nao'

def verificar_cpf_aluguel(cpf, objetos_aluguel, objetos_imovel):
    for x in objetos_aluguel:
        for y in objetos_imovel:
            if cpf == x.cpf and y.status == 'Sim':
                return True

def verificar_aluguel_cadastrado(codigo, excel_alugueis, excel_imoveis):
    for x, y in excel_alugueis.iterrows():
        for z, k in excel_imoveis.iterrows():
            if codigo == y['Codigo do Imovel'] and k['Status'] == 'Sim':
                return True

def verificar_alugado(codigo, objetos_aluguel, objetos_imovel):
    for x in objetos_aluguel:
        for y in objetos_imovel:
            if codigo == x.codigo and y.status == 'Sim':
                return True

def pegar_objeto_finalizar(cpf, codigo, objetos_aluguel):
    for x in objetos_aluguel:
        if cpf == x.cpf and codigo == x.codigo:
            objeto = x
            return objeto

def posicao_aluguel_dataframe(cpf, codigo, excel_alugueis):
    for x, y in excel_alugueis.iterrows():
        if cpf == y['CPF do Inquilino'] and codigo == y['Codigo do Imovel']:
            return x

def verificar_aluguel_inquilino(codigo, cpf, objetos_aluguel):
    for x in objetos_aluguel:
        if codigo == x.codigo and cpf == x.cpf:
            return True

def pegar_meses(data_entrada):

    data2 = date.today() #Aqui você pode validar as entradas, irei deixar pra você
    data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y").date()


    dias = data2 - data_entrada
    meses = dias.days // 30
    return meses