
def soma(a: float, b: float) -> float:
    return a + b

def subtracao(a: float, b: float) -> float:
    return a - b

def multiplicacao(a: float, b: float) -> float:
    return a * b

def divisao(a: float, b: float) -> float:
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def principal():
    menu_principal = """Escolha uma opção:
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Sair
    Opção: """
    
    op = int(input(menu_principal))
    while op != 5:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if op == 1:
            print(f"Resultado: {soma(a, b)}")
        elif op == 2:
            print(f"Resultado: {subtracao(a, b)}")
        elif op == 3:
            print(f"Resultado: {multiplicacao(a, b)}")
        elif op == 4:
            print(f"Resultado: {divisao(a, b)}")
        else:
            print("Opção inválida")

        op = int(input(menu_principal))

if __name__ == "__main__":
    principal()


