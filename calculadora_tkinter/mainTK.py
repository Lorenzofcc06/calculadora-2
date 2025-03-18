def menu():
    print("> Selecione uma operação <")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input("Digite o numero da operação que deseja fazer: "))

    return opcao

def numeros():
    try:

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

    except ValueError:
        print(">>> ERRO <<< Valor Inválido!")

    return num1,num2

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return ">>> ERRO <<< Não pode dividir por zero!"
    return a / b

def main():
    opcao = None
    num1 = None
    num2 = None

    while True:
        opcao = menu()

        if opcao == 5:
            break

        if opcao not in [1,2,3,4]:
           print("Opção Inválida!")
           continue

        num1, num2 = numeros()

        if opcao == 1:
           print(f'> Resultado da Soma: {somar(num1,num2)}')

        if opcao == 2:
          print(f'> Resultado da Subtração: {subtrair(num1,num2)}')
        
        if opcao == 3:
          print(f'> Resultado da Multiplicação: {multiplicar(num1,num2)}')

        if opcao == 4:
            print(f'> Resultado da Divisão: {dividir(num1,num2)}')
        
    print(">>> Execução Finalizada <<<")
main()