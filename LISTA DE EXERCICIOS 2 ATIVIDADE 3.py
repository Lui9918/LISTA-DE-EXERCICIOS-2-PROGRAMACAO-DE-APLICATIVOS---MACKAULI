#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

if __name__ == '__main__':

    m_or_f = input("Write M for male or F for female: ").upper()

    if m_or_f == "M":
        print("M - Male")
    elif m_or_f == "F":
        print("F - Female")
    else:
        print("Invalid sex")