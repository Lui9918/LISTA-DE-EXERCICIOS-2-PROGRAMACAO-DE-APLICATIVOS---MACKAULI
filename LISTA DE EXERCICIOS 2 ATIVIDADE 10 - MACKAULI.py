#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

if __name__ == '__main__':
    shift_study = input("What shift do you study? Write M for morning, A for afternoon, or E for evening: ").upper()

    if shift_study == "M":
        print("Good Morning!")
    elif shift_study == "A":
        print("Good Afternoon!")
    elif shift_study == "E":
        print("Good Evening!")
    else:
        print("Invalid value! Please try again.")
