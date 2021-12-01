from funcoes import Carregamento_Excel,Cadastro,Cadastro_Maq, Gerar_Codigo, desligar, dict_data

# ideia , e se eu localizar a posição da informação no dicionario e localizar as outras pela mesma posição da primeira ja que estão em ordem
dict_vendedor = {'Nome':[],'CPF':[],'Data de Nascimento':[],'Endereço':[]}
try :
    dict_vendedor = Carregamento_Excel('vendedores.xlsx','Nome')
except FileNotFoundError:
    pass

dict_maquinas = {'Código':['123'],'Descrição':['Trator'],'Preço Unitário':[200],'Quantidade de Estoque':[4]}
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

    if opcao == '4':
        opcao = str(input('''
    Colocar o Código:
    Manualmente...............[1]
    Geral Código Automatico...[2]
    \n\033[1;33mDigite sua opção: \033[m'''))

        if opcao == '1':
            codigo = str(input('Digite o código: '))

            if codigo not in dict_registro_venda['Código']:
                cpf = str(input('CPF do vendedor: '))

                if cpf in dict_vendedor['CPF']:
                    data = str(input('Data: '))

                elif cpf not in dict_vendedor['CPF']:
                    print('Esse CPF não foi cadastrado!')
            
            elif codigo in dict_registro_venda['Código']:
                print('Esse código já está sendo usado!')

        if opcao == '2':
            var = Gerar_Codigo()
            print(f'\nSeu código é: {var}')
            cpf = str(input('CPF do vendedor: '))

            if cpf in dict_vendedor['CPF']:
                data = str(input('Data: '))

            elif cpf not in dict_vendedor['CPF']:
                print('Esse CPF não foi cadastrado!')
        
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

'''
h) Relatório de Vendas; (1,0) 
i. Exibe todos as vendas registradas com as seguintes informações: Código  
da venda, Data da venda, Nome do vendedor, nome do cliente valor total  
da venda; 
ii. Para cada venda registrada deve exibir os itens vendidos logo abaixo com  
as seguintes informações: descrição da máquina, quantidade vendida, 
preço unitário, valor total do item de venda (quantidade * preço unitário); 
Código da venda: 1 
Data da venda:23/11/2021 
Nome do vendedor: João 
Nome do cliente: Maria 
Valor total da venda: 200,00
Descrição da máquina 	Quantidade vendida 	Preço unitário 	Valor total do item
Compressor 	2 	50,00 	100,00
Perfurador 	1 	100 	100,00
i) Relatório de Comissões; (1,0) 
a. Exibe todos as comissões calculadas para as vendas realizadas com as seguintes  informações: Código da venda, Data da venda, Nome do vendedor, valor total da  venda, valor da comissão. 
'''