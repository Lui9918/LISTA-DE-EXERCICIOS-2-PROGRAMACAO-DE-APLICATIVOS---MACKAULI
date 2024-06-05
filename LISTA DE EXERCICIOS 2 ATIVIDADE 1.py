#Faça um Programa que peça dois números e imprima o maior deles.

if __name__ == '__main__':

    first_number = float(input("To begin, write the first number: "))
    second_number = float(input("Now, write the second number: "))

    if first_number > second_number:
        print(f"The big number is {first_number}")
    elif second_number > first_number:
        print(f"The big number is {second_number}")
    else:
        print("The two numbers are equal")

