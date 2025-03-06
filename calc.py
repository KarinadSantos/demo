menu_principal = """
1- soma
2- subtracao
3- multiplicacao
4- divisao
5- resto
6- potenciacao
"""

def soma(a:float,b:float) -> float:
    return a + b

def subtracao(a:float,b:float) -> float:
    return a - b

def multiplicacao(a:float,b:float) -> float:
    return a * b

def divisao(a:float,b:float) -> float:
    if b == 0:
        return "Erro: divisao por 0"
    return a / b

def resto(a:float,b:float) -> float:
    return a % b

def potenciacao(a:float,b:float) -> float:
    return a ** b

def main():
    op = int(input(menu_principal))
    while op != 7:
        
            
            if op in[1,2,3,4,5,6]:
               a = float(input("Digite o primeiro número:"))
               b = float(input("Digite o segundo número:"))

            if op == 1 :
                print(f"Resultado: {soma(a,b)}")

            elif op == 2 :
                print(f"Resultado: {subtracao(a,b)}")

            elif op == 3 :
                print(f"Resultado: {multiplicacao(a,b)}")

            elif op == 4 :
                print(f"Resultado: {divisao(a,b)}")

            elif op == 5 :
                print(f"Resultado: {resto(a,b)}") 

            elif op == 6 :
                print(f"Resultado: {potenciacao(a,b)}") 

    else: 
            print("Opção inválida.tente novamente")

if __name__ == "__main__":
    main()
                


