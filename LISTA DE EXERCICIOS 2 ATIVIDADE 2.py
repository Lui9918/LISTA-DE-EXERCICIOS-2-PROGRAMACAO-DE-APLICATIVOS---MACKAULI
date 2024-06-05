#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

if __name__ == '__main__':
    value = float(input("To begin, write the value: "))

    if value > 0:
        print("The value are positive.")
    elif value < 0:
        print("The value are negative.")
    else:
        print("The value are zero.")

