import pandas as pd
#from tqdm import tqdm
#from time import sleep

def Carregamento_Excel(arquivo_excel, index_coluna):
    df = pd.read_excel(arquivo_excel)
    df.set_index(index_coluna).T.to_dict('list')
    return df.to_dict(orient='list')


#def Gerar_Codigo():
#    tamanho = 5
#    valores = string.ascii_lowercase + string.digits
#    codigo = ''
#    for i in range(tamanho):
#       codigo += choice(valores)

#   return codigo

#def desligar():
#    print('\nDesligando...')
#    try:
#        for i in tqdm(range(100)):
#            sleep(0.01)
#    except (NameError,ModuleNotFoundError):
#        pass

def dict_data(dicionario):
    df = pd.DataFrame(data=dicionario)
    return print(df)

class Cadastro:

    def __init__(self,dicionario,dicionario2,nome_arquivo):
        self.nome = str(input('\nNome: '))
        self.cpf = int(input('CPF: '))

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
        self.codigo = str(input('Digite o código (letras e numeros): '))

        if self.codigo not in dicionario['Código']:
            self.descricao = str(input('Descrição: '))
            self.preco = int(input('Valor Unitário: '))
            self.qtd = int(input('Quantidade de Estoque: '))
            dicionario['Código'] += [self.codigo]
            dicionario['Descrição'] += [self.descricao]
            dicionario['Preço Unitário'] += [self.preco]
            dicionario['Quantidade de Estoque'] += [self.qtd]

            df = pd.DataFrame(data=dicionario)
            df.to_excel(nome_arquivo,index=False)

            print(dicionario)
            print('\nCadastro de máquinas feito com sucesso!')

        elif self.codigo in dicionario['Código']:
            print('\nEsse Código já está sendo usado!')

