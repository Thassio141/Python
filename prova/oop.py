# class é o projeto do carro
# class nome_do_objeto:

class Car:
    # apos dizer oque precisa pra saber do carro , atribua metodos, como as funçoes que tem dentro do carro
    # ex : dirigir  e parar de dirigir
    # o __init__ é o metodo que vai contruir que vai construir objetos
    # para isso colocar as informações que necessita dentro do __init__
    # o __init__ é uma função então você deve chamar as variaveis dentro dela como uma função normal faria
    # para que funcione ao meniconar a variavel na função coloque o "self." na frente.
    # apos colocar o self.x é necessario colocar oque deve fazer cada self ,ou seja , self.fabricante = fabricante
    # assim como em uma função normal

    rodas = 4

    # se colocarmos uma variavel fora do __init__ , porem dentro da classe , temos então que todos os carros tem 4 rodas
    # variavel default (padrão)
    def __init__(self, fabricante, modelo, ano, cor):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    # pelo que entendi usar o self.x , é como criar uma variavel dentro de uma função que não conseguiamos antes

    '''def dirigir(self):  # usar o self é padrão
        print('This car is driving')

    def parar(self):
        print('This car is stopped')'''

    # Ok , agora vimos que podemos descobrir tudo em ordem , porem podemos melhorar algumas coisas

    # colocando o self.modelo entre a frase podemos assim distinguir os carros que estão sendo dirigitdos,
    # o format tmb funciona

    def dirigir(self):
        print('This ' + self.modelo + ' is driving')

    def parar(self):
        print('This ' + self.modelo + ' is stopped')


# a partir daqui é a tentativa de utilizar as funções

carro_1 = Car('Chevrolet', 'Corvette', 2021, 'azul')
print(carro_1.fabricante)
print(carro_1.modelo)
print(carro_1.ano)
print(carro_1.cor)
print(carro_1.fabricante, carro_1.modelo, carro_1.ano, carro_1.cor)

# se decidirmos trocar a variavel do class você pode utilizar carro_x.rodas ou pode mudar a variavel de maneira geral
# ex:
Car.rodas = 2
carro_1.dirigir()
carro_1.parar()
# carro_1.rodas = 4
print(carro_1.rodas)

carro_2 = Car('Ford', 'Mustang', 2022, 'red')
carro_2.dirigir()
carro_2.parar()
# carro_2.rodas = 2
print(carro_2.rodas)
