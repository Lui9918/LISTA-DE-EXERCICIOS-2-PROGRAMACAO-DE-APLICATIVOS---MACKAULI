#Faça um Programa que leia três números e mostre-os em ordem decrescente.

if __name__ == '__main__':
    first_number = float(input("To begin, write the first number: "))
    second_number = float(input("Now, write the second number: "))
    third_number = float(input("To finish, write the third number: "))

    # Encontra o maior número
    max_number = max(first_number, second_number, third_number)

    # Encontra o menor número
    min_number = min(first_number, second_number, third_number)

    # Encontra o número do meio
    middle_number = (first_number + second_number + third_number) - max_number - min_number

    # Exibe os números em ordem decrescente
    print("The numbers in descending order are:")
    print(max_number)
    print(middle_number)
    print(min_number)
