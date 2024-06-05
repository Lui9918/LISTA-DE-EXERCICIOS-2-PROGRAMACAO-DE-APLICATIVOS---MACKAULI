#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

if __name__ == '__main__':
    week_day = int(input("Write number for the day of the week, for example: 1 for Sunday, 2 for Monday, 3 for Tuesday, 4 for Wednesday, 5 for Thursday, 6 for Friday and 7 for Saturday: "))

    if week_day == 1:
        print("Sunday")
    elif week_day == 2:
        print("Monday")
    elif week_day == 3:
        print("Tuesday")
    elif week_day == 4:
        print("Wednesday")
    elif week_day == 5:
        print("Thursday")
    elif week_day == 6:
        print("Friday")
    elif week_day == 7:
        print("Saturday")
    else:
        print("Value invalid")