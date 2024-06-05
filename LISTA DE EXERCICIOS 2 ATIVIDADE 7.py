#Faça um Programa que leia três números e mostre o maior e o menor deles.

if __name__ == '__main__':
    first_number = float(input("To begin, write the first number: "))
    second_number = float(input("Now, write the second number: "))
    third_number = float(input("To finish, write the third number: "))

    if first_number <= second_number and first_number <= third_number:
        print(f"The smallest number is {first_number}")
    elif second_number <= first_number and second_number <= third_number:
        print(f"The smallest number is {second_number}")
    else:
        print(f"The smallest number is{third_number}")