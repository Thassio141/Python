import pandas as pd
import string
from tqdm import tqdm
from time import sleep
from random import choice

def Carregamento_Excel(arquivo_excel, index_coluna):
    df = pd.read_excel(arquivo_excel)   
    df.set_index(index_coluna).T.to_dict('list')
    return df.to_dict(orient='list')


def Gerar_Codigo():
    tamanho = 5
    valores = string.ascii_lowercase + string.digits
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)

    return senha

def desligar():
    print('\nDesligando...')
    try:
        for i in tqdm(range(100)):
            sleep(0.01)
    except (NameError,ModuleNotFoundError):
        pass

def dict_data(dicionario):
    df = pd.DataFrame(data=dicionario)
    return print(df)

class Cadastro:
    #colocar 4 items para incluir
    def __init__(self,dicionario,dicionario2,nome_arquivo):
        self.nome = str(input('\nNome: '))
        self.cpf = str(input('CPF: '))

        if self.cpf not in dicionario['CPF'] and self.cpf not in dicionario2['CPF']:
            self.data = str(input('Data de nascimento: '))
            self.endereco = str(input('Endereço: '))
            dicionario['CPF'] += [self.cpf]
            dicionario['Nome'] += [self.nome]
            dicionario['Data de Nascimento'] += [self.data]
            dicionario['Endereço'] += [self.endereco]

            df = pd.DataFrame(data=dicionario)
            df.to_excel(nome_arquivo,index=False)

            print(dicionario)
            print('\nCadastro feito com sucesso!')

        elif self.cpf in dicionario['CPF'] or self.cpf in dicionario2['CPF']:
            print('\nEsse CPF já está cadastrado.')

class Cadastro_Maq:
    def __init__(self,dicionario,nome_arquivo):
        self.codigo = str(input('Código: '))

        if self.codigo not in dicionario['Código']:
            self.descricao = str(input('Descrição: '))
            self.preco = int(input('Valor Unitário: '))
            self.qtd = int(input('Quantidade de Estoque: '))
            
            df = pd.DataFrame(data=dicionario)
            df.to_excel(nome_arquivo,index=False)
            
            print(dicionario)
            print('\nCadastro de máquinas feito com sucesso!')

        elif self.codigo in dicionario['Código']:
            print('\nEsse Código já está sendo usado!')

class Relatorio:
    #colocar 4 items para mostrar
    pass

    #ModuleNotFoundError