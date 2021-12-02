from funcoes import Carregamento_Excel,Cadastro,Cadastro_Maq, Gerar_Codigo, desligar, dict_data

# ideia , e se eu localizar a posição da informação no dicionario e localizar as outras pela mesma posição da primeira ja que estão em ordem
dict_vendedor = {'Nome':[],'CPF':[],'Data de Nascimento':[],'Endereço':[]}
try :
    dict_vendedor = Carregamento_Excel('vendedores.xlsx','Nome')
except FileNotFoundError:
    pass

dict_maquinas = {'Código':[],'Descrição':[],'Preço Unitário':[],'Quantidade de Estoque':[]}
try:
    dict_maquinas = Carregamento_Excel('maquinas.xlsx','Código')
except FileNotFoundError:
    pass

dict_cliente = {'Nome':[],'CPF':[],'Data de Nascimento':[],'Endereço':[]}
try:
    dict_cliente = Carregamento_Excel('clientes.xlsx','Nome')
except FileNotFoundError:
    pass

dict_registro_venda = {'Código':[],'CPF Vendedor':[],'Data da Venda':[]} 
try:
    dict_registro_venda = Carregamento_Excel('registro_vendas.xlsx','Código')
except FileNotFoundError:
    pass

while True:

    opcao = str(input('''
\nCadastrar Vendedor.......[1]
Cadastrar Maquinas.......[2]
Cadastrar Clientes.......[3]
Registrar Venda..........[4]
Relatório de Vendedores..[5]
Relatório de Máquinas....[6]
Relatório de Clientes....[7]
Relatório de Vendas......[8]
Relatório de Comissões...[9]
Sair.....................[10]
    \n\033[1;33mDigite sua opção: \033[m'''))

    if opcao == '1':
        Cadastro(dict_vendedor,dict_cliente,'vendedores.xlsx')

    if opcao == '2':
        Cadastro_Maq(dict_maquinas,'maquinas.xlsx')

    if opcao == '3':
        Cadastro(dict_cliente,dict_vendedor,'clientes.xlsx')

    '''
    b. Após isso deverá informar os itens a serem registrados nessa venda: código da  máquina, quantidade vendida; deve permitir inserir mais de um item na venda; 
    c. Os valores de CPF do vendedor, CPF do cliente e código da máquina devem ser  válidos, ou sejam, devem estar cadastrados no sistema; 
    d. Quando ocorre o registro da venda, o cadastro da máquina deve ser atualizado  para que a quantidade de estoque seja baixada; 
    '''
    if opcao == '4':
        codigo = str(input('Digite o código de venda(letras e números): '))

        if codigo not in dict_registro_venda['Código']:
            cpf = int(input('CPF do vendedor: '))

            if cpf in dict_vendedor['CPF']:
                data = str(input('Data: '))
                print('\n')
                dict_data(dict_maquinas)
                
                while True:
                    codigo = str(input('Código da máquina(letras e números): '))
                    if codigo in dict_maquinas['Código']:
                        qtd = int(input('Quantidade de máquinas que deseja comprar: '))
                        
                        if qtd > x:# quantidade registrada no dicionario
                            pass

                        else:
                            pass
                            # reduzir do cpf e do dicionario
                    
                    elif codigo not in dict_maquinas['Código']:
                        print('Máquina não cadastrada!')
                    
                    
            elif cpf not in dict_vendedor['CPF']:
                print('Esse CPF não foi cadastrado!')
        
        elif codigo in dict_registro_venda['Código']:
            print('Esse código já está sendo usado!')
        
    if opcao == '5':
        dict_data(dict_vendedor)
    
    if opcao == '6':
        dict_data(dict_maquinas)
        
    if opcao == '7':
        dict_data(dict_cliente)
    
    if opcao == '8':
        pass

    if opcao == '9':
        pass

    if opcao == '10':
        desligar()
        break