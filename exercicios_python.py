# -*- coding: utf-8 -*-
"""

######################################################################
########## Código desenvolvido por: Gustavo Baron Lauritzen ##########
######################################################################

1.	Faça um código que peça um número e então mostre a mensagem: ***O número informado foi [número]***
"""
numero = int(input("Digite um número:"))
print("O número digitado foi", numero)

"""2.	Faça um código que peça dois números e imprima a soma.
"""
numero1 = 10
numero2 = 5
soma = numero1 + numero2

"""3.	Faça um código que peça as 4 notas bimestrais e mostre a média.
"""
nota1 = int(input("Primeira nota: "))
nota2 = int(input("Segunda nota: "))
nota3 = int(input("Terceira nota: "))
nota4 = int(input("Quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média foi de: ",media)

"""4.	Faça um código que peça o raio de um círculo, calcule e mostre sua área.
"""
import math
raio = int(input("Digite o raio: "))
area = 3.14 * (raio ** 2)
print("Área total: ", area)

"""5.	Faça um código que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
import math
lado =  int(input("Digite o valor de um dos lados do quadrado: "))
A = lado ** 2
print("A área do quadrado é:", A)

"""6.	Faça um código que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
"""
faren =  int(input("Digite o valor da temperatura em Farenheit: "))
celsius = (faren - 32) * 5/9
print("A temperatura em graus celsius é:", celsius , "graus")

"""7.	Faça um código que peça 2 números inteiros e um número real, calcule e mostre:

          a.	O produto do dobro do primeiro com metade do segundo.
          b.	A soma do triplo do primeiro com o terceiro.
          c.	O terceiro elevado ao cubo.
"""
import math
num1 = int(input("Digite o 1 numero: "))
num2 = int(input("Digite o 2 numero: "))
num3 = float(input("Digite o 3 numero: "))
a = (num1 ** 2) * (num2 / 2)
b = (num1 ** 3) + num3
c = num3 ** 3
print(a, b, c)

"""8.	João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 

> João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
peso = float(input("Digite o peso: "))
if(peso > 50):
  excesso = peso - 50
  multa = 4 * excesso
print("Peso: ", peso)
print("Excesso: ", excesso)
print("Valor da multa: ", multa)

"""9.	Faça um código que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
          a.	Salário bruto.
          b.	Quanto pagou ao INSS.
          c.	Quanto pagou ao sindicato.
          d.	O salário líquido.
        	Calcule os descontos e o salário líquido, conforme abaixo:
	        (+) Salário Bruto
	        (-) IR (11%)
	        (-) INSS (8%)
	        (-) Sindicato (5%)
            (=) Salário Liquido
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
hora = float(input("Quanto você ganha por hora? "))
numero_de_horas = float(input("Quantidade de horas trabalhadas no mês:"))
salario_bruto = hora * numero_de_horas
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
imposto_de_renda = salario_bruto * 0.11
salario_liquido = salario_bruto - inss - sindicato - imposto_de_renda
print("Salário Bruto: ", salario_bruto)
print("Valor INSS: ", inss)
print("Valor Sindicato: ", sindicato)
print("Valor Imposto de Renda : ", imposto_de_renda)
print("Salário Líquido: ", salario_liquido)

"""10.	Faça um código para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math
tamanho = float(input("Digite o tamanho(em metros quadrados) da área a ser pintada: "))
litros_de_tinta = tamanho / 3
qtd_latas = math.ceil(litros_de_tinta / 18)
preco_total = qtd_latas * 80.00
print("Quantidade de latas de tinta:", qtd_latas)
print("Preço total:", preco_total, "reais")

"""11.	Faça um código para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 80 reais ou em galões de 3,6 litros, que custam 25 reais.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

      Comprar apenas latas de 18 litros;
      Comprar apenas galões de 3,6 litros;
      Misturar latas e galões, de forma que o preço seja o menor. 
      
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
"""
import math
tamanho = float(input("Digite o tamanho(em metros quadrados) da área a ser pintada: "))
litros_de_tinta = tamanho / 6
qtd_latas = math.ceil(litros_de_tinta / 18)
qtd_galao = math.ceil(litros_de_tinta / 3.6)
preco_total_latas = qtd_latas * 80.00
preco_total_galao = qtd_galao * 25.00
print("Litros de tinta:", litros_de_tinta)
print("Preço apenas em latas", preco_total_latas)
print("Preço apenas em galões", preco_total_galao)

"""12.	Faça um código que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamArquivo = float(input("Tamanho: "))
velocidadeI = float(input("Velocidade: "))
tamArquivoMbits = tamArquivo * 8
tempoEmSegundos = (tamArquivoMbits / velocidadeI) 
tempo = tempoEmSegundos / 60
print("Tempo em minutos do download:", tempo)

"""
13.	Faça um código que leia 5 números, guarde em uma lista e depois informe o maior deles.
"""
lista = []
for i in range(5):
  lista.append(float(input("Digite um número:")))
maior = 0
for i in range(5):
  if lista[i] > maior:
    maior = lista[i]
print("O número maior é:",maior)

"""14.	Faça um código que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

  	    Dicas:

          *   Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
          *   Triângulo Equilátero: três lados iguais;
          *   Triângulo Isósceles: quaisquer dois lados iguais;
          *   Triângulo Escaleno: três lados diferentes.
"""
lados = []
for i in range(3):
  lados.append(float(input("Digite um número: ")))
soma = lados[0] + lados[1] 
soma2 = lados[0] + lados[2]
soma3 = lados[1] + lados[2]
if soma > lados[2] and soma2 > lados[1] and soma3 > lados[0]:
  print("Isso é um triângulo :)")
  if lados[0] == lados[1] and lados[0] == lados[2] and lados[1] == lados[2]:
    print("Triângulo equilátero")
  elif lados[0] != lados[1] and lados[0] != lados[2] and lados[1] != lados[2]:
    print("Triângulo escaleno")
  else:
    print("Triângulo isósceles")
else:
  print("Isso não é um triângulo :(")

"""15.	Faça um código que peça um valor e mostre se ele é primo."""
v = (int(input("Digite um número: ")))
resposta=1
for i in range(2,v):
  if(v % i == 0):
    resposta = 0
if(resposta == 1):
  print("É um número primo")
else:
  print("Não é um número primo")

"""16.	Sendo `H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N`, Faça um código que calcule o valor de H com N termos."""
n =  int(input("Digite o n aqui:"))
h = 0
for i in range(1,n+1):
  h = h + 1/i 
  print(h)

"""17.	Faça um código que leia um vetor de 10 caracteres e diga quantas consoantes foram lidas. Imprima as consoantes."""
caract=[]
vogais=["a","e","i","o","u"]
consoantes = []
x = 1
while x <= 10:
    entrada = input("Insira uma letra:")
    x += 1
    caract.append(entrada)
    if entrada not in vogais:
        consoantes.append(entrada)
print("Quantidade de consoantes: ",(len(consoantes)))
print("Consoantes:", consoantes)

"""18.	Faça um código que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

  *   Mostre a quantidade de valores que foram lidos;
  *   Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
  *   Calcule e mostre a soma dos valores;
  *   Calcule e mostre a média dos valores;
  *   Calcule e mostre a quantidade de valores acima da média calculada;
  *   Calcule e mostre a quantidade de valores abaixo de sete;
"""
notas = []
notas_abaixo = []
notas_acima = []
qtd_valor = 0
fim = False
soma = 0
media = 0
while(fim == False):
  entrada = int(input("Informe uma nota(para encerrar digite '-1'):"))
  if entrada == -1:
    fim = True
  if entrada != -1:
    notas.append(entrada)
    qtd_valor += 1
    soma = soma + entrada
media = soma / qtd_valor
for i in range(len(notas)):
  if notas[i] > media:
    notas_acima.append(notas[i])
  if notas[i] < 7:
    notas_abaixo.append(notas[i])
  i+=1
print("Quantidade de valores lidos:", qtd_valor)
print("Valores na ordem em que foram informados:",notas)
print("Soma dos valores:", soma)
print("Média dos valores:",media)
print("Notas acima da média calculada:", len(notas_acima))
print("Notas abaixo de 7:", len(notas_abaixo))

"""
19. Escreva uma função chamada `num_teste` que aceite um número como entrada. Se o número for maior que 10, a função retornará `"Maior que 10."` Se o número for menor que 10, a função retornará `"Menor que 10."` Se o número for igual a 10, a função deve retornar `"Igual a 10."`
"""
def num_teste(num):
  if(num > 10):
    print("Maior que 10.")
  elif(num < 10):
    print("Menor que 10.")
  else:
    print("Igual a 10.")
num = int(input("Digite um número: "))
num_teste(num)

"""20.   Escreva uma função `soma_quadrados(lista)` que calcule a soma dos quadrados dos números na lista lista. Por exemplo, `som_quadrados([2, 3, 4])` deve retornar `4 + 9 + 16`, que é `29`."""
import math
def soma_quadrados(lista):
  soma = 0
  for num in lista:
    soma = soma + num * num
  return soma
lista = [2,3,4]
print(soma_quadrados(lista))

"""21.   Escreva uma função que retorna o número de dígitos de um inteiro.
"""
print(round(13.2 - 13, 2) == 0.2)

"""22.   Faça uma função que receba uma string de texto e, começando com um dicionário vazio, faça com que ele tenha como chave as letras do alfabeto e como valor a quantidade de vezes que ela aparece no texto. Cada letra somente deve ser adicionada ao dicionário a primeira vez que ela aparece no texto."""
alfabeto = "abcdefghijklmnopqrstuvwxyz"
def contagem_letras(texto):
  dicionario = {}
  texto = texto.lower()
  for letra in texto:
    if letra in dicionario:
      dicionario[letra] = dicionario[letra] + 1
    else:
      dicionario[letra] = 1
  return dicionario
texto = "Cada letra somente dvee ser"
contagem = contagem_letras(texto)
print(contagem)

"""23.   Faça uma função que receba o dicionário do problema anterior e adicione as vogais que não apareceram no texto com o valor 0.
"""
vogais = "aeiou"
def adicionar_vogais(dicionario,):
  inteiro = 0
  for vogal in vogais:
    if vogal not in dicionario:
      dicionario[vogal] = 0
contagem = contagem_letras(texto)
print(contagem)
adicionar_vogais(contagem)
print(contagem)

"""24.   Um posto está vendendo combustíveis com a seguinte tabela de descontos:

*   Álcool: até 20 litros, desconto de 3% por litro e acima de 20 litros, desconto de 5% por litro;
*   Gasolina: até 20 litros, desconto de 4% por litro e acima de 20 litros, desconto
de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (A-álcool, G-gasolina) e imprima o valor a ser pago pelo cliente.
Considere que o preço do litro da gasolina é 2,49 e o preço do litro do álcool é R$ 1,69.
"""
desconto = 0
preco_total = 0
valor_litros = int(input("Qual é o valor total de litros vendidos? "))
tipo_combustivel = input("Qual é o tipo de combustível? Obs: Digite 'A' para álcool e 'G' para gasolina. ")
verifica_combustivel = True
if tipo_combustivel == 'G':
  if(valor_litros <= 20):
    desconto = (valor_litros*2.49) * 0.04
  else:
    desconto = (valor_litros*2.49) * 0.06    
  preco_total = (valor_litros*2.49) - desconto
  pass
elif tipo_combustivel == 'A':
  if(valor_litros <= 20):
    desconto = (valor_litros*1.69) * 0.03
  else:
    desconto = (valor_litros*1.69) * 0.05
  preco_total = (valor_litros*1.69) - desconto
  pass
else:
  print("Desculpe, mas esse tipo de cobustível não existe!")
  verifica_combustivel = False
  pass
if(verifica_combustivel == True):
  print("O valor total a ser pago pelo cliente é de: R$", round(preco_total, 2))

"""25.   Escreva um algoritmo que solicite ao usuário um valor (total) em dinheiro, e informe a quantidade de notas de: 2 reais, 5 reais, 10 reais, 20 reais, 50 reais e 100 reais, e a quantidade de moedas de: 1 real, 50 centavos, 25 centavos, 10 centavos e 1 centavo que serão
necessárias para compor este valor, de forma que seja utilizado o menor número de notas e moedas possível.
"""
valor = float(input("Informe o valor em dinheiro: "))
moedas = [1.00, 0.50, 0.25, 0.10, 0.01]
notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
quantidade_notas = []
quantidade_moedas = []
while True:
  for i in range(6):
    quantidade_notas.append(int(valor / notas[i]))
    valor = valor % notas[i]
  if(valor < 2.00):
    break
while True:
  for i in range(5):
    quantidade_moedas.append(int(valor / moedas[i]))
    valor = valor % moedas[i]
  if(valor < 0.001):
    break
  else:
    quantidade_moedas[4] += 1
    break  
print("Você precisará de:\n", quantidade_notas[0], " cédula(s) de R$100,00\n",
      quantidade_notas[1], " cédula(s) de R$50,00\n", quantidade_notas[2], " cédula(s) de R$20,00\n", 
      quantidade_notas[3], " cédula(s) de R$10,00\n", quantidade_notas[4], " cédula(s) de R$5,00\n",
      quantidade_notas[5], " cédula(s) de R$2,00\n", quantidade_moedas[0], " moeda(s) de R$1,00\n",
      quantidade_moedas[1], " moeda(s) de R$0,50\n", quantidade_moedas[2], " moeda(s) de R$0,25\n",
      quantidade_moedas[3], " moeda(s) de R$0,10\n", quantidade_moedas[4], " moeda(s) de R$0,01\n")

"""26.   Faça um algoritmo que verifique e escreva todos os números inteiros perfeitos entre 1 a 10000.
*Um número se diz perfeito se é igual à soma de seus divisores próprios. Divisores próprios de um número positivo N são todos os divisores inteiros positivos de N exceto o próprio N. Por exemplo, o número 6, seus divisores próprios são 1, 2 e 3, cuja soma é igual à 6. 28 também é um número perfeito, já que é divisível por 1, 2, 4, 7, 14*
"""
print('Os números perfeitos entre 1 e 10000 são: ')
for val in range(1,10000+1):
  soma = 0
  for i in range(1,val):
    if val % i == 0:
        soma += i
  if val==soma:
      print(val)

"""27.   A cifra de César é uma cifra de substituição simples em que cada letra do texto é substituída por outra letra movendo `n` posições no alfabeto. Por exemplo, suponha que o texto simples de entrada seja o seguinte:

`abcd xyz bola`

Se o valor de deslocamento, n, for 4, o texto criptografado seria o seguinte:

`efgh bcd fspe`

Escreva uma programa que tenha uma mensagem de texto simples e um número de letras para deslocar na cifra. Ela deve fazer uma string criptografada com todas as letras transformadas e toda a pontuação e espaço em branco permanecendo inalterados.
Nota: Você pode presumir que o texto simples é todo em minúsculas, exceto para espaços em branco e pontuação.
Podem criam uma string `alfabeto="abcdefghijklmnopqrstuvwxyz"` para auxiliar.
"""
# coding utf-8
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
entrada= input("Digite a mensagem a ser criptografada:\n")
entrada = entrada.lower()
deslocamento = int(input("Qual é a quantidade de deslocamento?\n"))
while deslocamento > 26 or deslocamento < 0:  
  print(" ")
  deslocamento = input("Deslocamento inválido, tente novamente: ")
final = ""
for palavra in entrada:
  if(palavra in alfabeto):
    posicao = alfabeto.find(palavra)
    posicao += deslocamento
    if(posicao > 26):
        posicao = posicao - 26
    final = final + alfabeto[posicao]
  else:
    final = final + palavra
print("Sua palavra criptografa é:")
print(final)