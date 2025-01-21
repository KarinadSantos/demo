#q1
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
 

if num1 > num2:
    maior_num = num1
else:
    maior_num = num2
 
print("O maior número é:", maior_num)


#q2
num =  int(input("digite o numero:"))

positivo = (num)
negativo =-(num)

print(f"Valor positivo:{positivo}")
print(f"Valor negativo:{negativo}")


#q3
letra = input("F ou M:") .upper()

if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")

else:
    print("sexo inválido")

#q4
letra = input("Digite uma letra: ").lower()

if len(letra) == 1:  
    if letra in "aeiou":
        print("A letra digitada é uma vogal.")
    else:
        print("A letra digitada é uma consoante.")
else:
    print("Entrada inválida. Digite apenas uma letra.")


#q5
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = (nota1 + nota2) / 2


if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


#q6
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3= int(input("Digite o terceiro número: "))

maior_num = num1
 
if num2 > maior_num:
    maior_num = num2
 
if num3 > maior_num:
    maior_num = num3

print("O maior número é:", maior_num)


#q7
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))


maior_num = num1
if num2 > maior_num:
    maior_num = num2
if num3 > maior_num:
    maior_num = num3

menor_num = num1
if num2 < menor_num:
    menor_num = num2
if num3 < menor_num:
    menor_num = num3

print("O maior número é:", maior_num)
print("O menor número é:", menor_num)


#q8
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

if preco1 < preco2 and preco1 < preco3:
    print("Você deve comprar o primeiro produto.")
elif preco2 < preco1 and preco2 < preco3:
    print("Você deve comprar o segundo produto.")
elif preco3 < preco1 and preco3 < preco2:
    print("Você deve comprar o terceiro produto.")


#q9
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


numeros = [num1, num2, num3]


numeros.sort(reverse=True)


print("Números em ordem decrescente:", numeros)


#q10
turno = input("Em que turno você estuda?:").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")