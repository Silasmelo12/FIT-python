import numpy as np

# Utilize os valores de n1 = 2, n2 = 3, n3 = -1 e n4 = 8 e verifique se as
#
# expressões lógicas a seguir resultam em True ou False.
#
# a. n1 < n3
# b. n3 == n4
# c. n1 + n2 > n3
# d. n3 / n1 < n4
# e. n1 + n2 < 10 and n3 - n4 == n1
# f. n3 / n2 > 0 or n1 + n3 > n4
def exLogicas():
    n1 = 2
    n2 = 3
    n3 = -1
    n4 = 8
    print("a. n1 < n3: ",n1 < n3)
    print("b. n3 == n4: ",n3 == n4)
    print("c. n1 + n2 > n3: ",n1 + n2 > n3)
    print("d. n3 / n1 < n4: ",n3 / n1 < n4)
    print("e. n1 + n2 < 10 and n3 - n4 == n1: ",n1 + n2 < 10 and n3 - n4 == n1)
    print("f. n3 / n2 > 0 or n1 + n3 > n4: ",n3/n2 > 0 or n1 + n3 > n4)
# Armazene três números nas variáveis “a”, “b” e “c” e resolva as seguintes
# equações utilizando a linguagem de programação Python:
#
#  r = a + b - c
#  r = a * (b + c)
#  r = (a + b) / c
#  r = (a + b + c) / 3
def abcEquation():

    a = float(input("Informe o valor de a: "))
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))
    r1 = a+b-c
    r2 = a*(b+c)
    r3 = (a+b)/c
    r4 = (a+b+c)/3
    print("r = a+b-c = ",    r1)
    print("r = a*(b+c) = ",  r2)
    print("r = (a+b)/c = ",  r3)
    print("r = (a+b+c)/3 = ",r4)
# Escreva um programa em Python que solicita ao usuário que digite seu nome,
# e em seguida armazena em uma variável o que foi digitado, exibindo uma mensagem personalizada na tela.
def informarNome():
    nome = input("Informe o seu nome: ")
    print("Bom dia Sr(a).",nome)

# Escreva um programa em Python que recebe dois números
# e mostra o resultado da soma e a diferença entre os dois.
def somar_e_subtrair():
    x = input("Informe o valor de x: ")
    y = input("Informe o valor de y: ")
    adicao = float(x)+float(y)
    subtracao = float(x)-float(y)
    print("O valor da adicao é: ", adicao)
    print("O valor da subtracao é: ", subtracao)

# ==============

# Escreva um programa que decide se um número é par ou ímpar.
def parImpar():
    n = input("Informe um número: ")
    if(float(n)%2==0):
        print("O número ",n," é par.")
    else:
        print("O número ", n, " é ímpar.")

# Escreva um programa que classifique um atleta em uma categoria etária,
# de acordo com a tabela a seguir:
def classificarAtleta():
    idade = float(input("Informe a idade do atleta: "))
    if (idade >= 5 and idade <= 10):
        print("O atleta é Infantil.")
    elif (idade >= 11 and idade <= 17):
        print("O atleta é Júnior.")
    elif (idade >= 18 and idade <= 30):
        print("O atleta é Profissional.")
    elif (idade > 30):
        print("O atleta é Sênior.")

def impar100():
    for n in range(100):
        if (n%2!=0):
            print(n)

def nomeIdade():

    while (True):

        nome = input("Informe o nome: ")

        if (nome == 'fim'):
            print("Obrigado pela preferência, volte sempre!")
            break

        idade = float(input("Informe a idade: "))
        print("Seja bem vindo ", nome," sua idade é: ",idade)

# Construa duas listas e mostre as listas na tela.
# Depois, crie uma lista a partir da junção das duas listas anteriores e mostre o valor da posição 0.
def listas():
    lista1 = ["a","b","c"]
    lista2 = ["d","e","f"]

    print("Lista 1: ",lista1)
    print("Lista 2: ",lista2)

    lista3 = lista1+lista2

    print("Posicao 0 da lista juntada: ",lista3[0])

# Construa um dicionário cujas chaves sejam as palavras em inglês for, in, if, else, True, False e while
# e os valores sejam as traduções para o português.

def dic():
    dic = {'for':"Para", 'in':"Em", 'if':"Se", 'else':"Se não",
           'True':"Verdadeiro", 'False':"Falso",'while':"Enquanto"}
    print(dic)

def somar(a,b):
    return a + b

def media(lista):
    soma = 0;
    for n in lista:
        soma +=n;
    return soma / len(lista)

# Crie uma classe Animais com as propriedades nome,
# raça e ano de nascimento. Instancie os objetos gato,
# cachorro e passarinho e crie um método para calcular a idade dos animais.
class Animais:
    nome = ""
    raça = ""
    anoNascimento = 0

    def idadeAnimal(self,anoNascimento):
        return 2022 - anoNascimento

def dimensaoMatrix():
    A = np.matrix([1, -1, 1])
    B = np.matrix([[2, 1, 1],
                  [1, 2, -5]])
    C = np.matrix([[1, 4],[2, 4]])
    print(A)
    print(B)
    print(C)
    dimA = A.shape
    dimB = B.shape
    dimC = C.shape
    print('Dimensões matriciais: A{}'.format(dimA))
    print('Dimensões matriciais: B{}'.format(dimB))
    print('Dimensões matriciais: C{}'.format(dimC))

def transposta():
    A = np.matrix([[6,1,3,2],[1,5,2,1],[7,0,2,1],[1,2,3,4]])
    B = np.matrix([[2,1,1],[1,3,2]])
    print("A = ",A)
    print("Transposta de A: \n",A.T)
    print("B = ",B)
    print("Transposta de B: \n",B.T)

def norma():
    X = np.matrix([1,2,3,4])
    norma = np.linalg.norm(X)
    print("Norma do vetor X = ",X," é ",norma," ",np.type)

if __name__ == '__main__':

    dimensaoMatrix()
    transposta()
    norma()
    # parImpar()
    # classificarAtleta()
    # impar100()
    # nomeIdade()
    # listas()
    # dic()
    # print(somar(float(input("Informe o valor de a: ")),float(input("Informe o valor de b: "))))
    # print("Média da lista: [1,2,3,4]: ",media([1,2,3,4]))
    #
    # gato = Animais()
    # gato.nome = "Zefa"
    # gato.raça = "Vira lata"
    # gato.anoNascimento = 2010
    #
    # cachorro = Animais()
    # cachorro.nome = "Jack"
    # cachorro.raça = "Pudle"
    # cachorro.anoNascimento = 2015
    #
    # passarinho = Animais()
    # passarinho.nome = "Pirulito"
    # passarinho.raça = "Tiziu"
    # passarinho.anoNascimento = 2020
    #
    # lista = [gato,cachorro,passarinho]
    #
    # for i in range(3):
    #     print("A idade de ",lista[i].nome," é: ",lista[i].idadeAnimal(lista[i].anoNascimento))
