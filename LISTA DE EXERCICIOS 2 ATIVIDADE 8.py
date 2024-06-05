#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

if __name__ == '__main__':
    first_price = float(input("To begin, write the first price of the product: "))
    second_price = float(input("Now, write the second price of the product: "))
    third_price = float(input("To finish, write the third price of the product: "))

    if first_price <= second_price and first_price <= third_price:
        print(f"The smallest number is {first_price}, you should buy this")
    elif second_price <= first_price and second_price <= third_price:
        print(f"The smallest price is {second_price}, you should buy this")
    else:
        print(f"The smallest price is{third_price}, you should buy this")