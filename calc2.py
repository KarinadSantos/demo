menu_principal = '''
1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- resto
6- potenciação
7- Sair
Escolha uma opção:
'''

def soma(a: float, b: float) -> float: 
    return a + b

def subtração(a: float, b: float) -> float: 
    return a - b

def multiplicação(a: float, b: float) -> float: 
    return a * b

def divisão(a: float, b: float) -> float: 
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def resto(a: float, b: float) -> float: 
    return a % b

def potenciação(a: float, b: float) -> float: 
    return a ** b


def main():
    op = 0
    while op != 7:
        op = int(input(menu_principal))

        if op in [1, 2, 3, 4, 5, 6]: 
            a = float(input("Digite o primeiro número: ")) 
            b = float(input("Digite o segundo número: ")) 

            if op == 1: 
                print(f"Resultado: {soma(a, b)}")

            elif op == 2: 
                print(f"Resultado: {subtração(a, b)}")

            elif op == 3: 
                print(f"Resultado: {multiplicação(a, b)}")

            elif op == 4: 
                print(f"Resultado: {divisão(a, b)}")

            elif op == 5: 
                print(f"Resultado: {resto(a, b)}")

            elif op == 6: 
                print(f"Resultado: {potenciação(a, b)}")

        else:  
            print("Opção inválida")

if __name__ == "__main__":
    main()
