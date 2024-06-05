#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

if __name__ == '__main__':
    letter = input("Write one letter: ")

    if letter in "aeiou":
        print("Your letter is a vowel")
    else:
        print("Your letter is a consonant")
