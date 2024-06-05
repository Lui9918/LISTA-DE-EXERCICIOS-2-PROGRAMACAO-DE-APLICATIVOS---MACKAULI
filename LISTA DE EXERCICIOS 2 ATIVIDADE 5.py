#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

if __name__ == '__main__':
    first_grade = float(input("To begin, write your first grade: "))
    second_grade = float(input("Now, write your second grade: "))

    grade_average = (first_grade + second_grade) / 2

    if grade_average == 10:
        print("You are approved with distinction")
    elif grade_average >= 7:
        print("You are approved")
    else:
        print("You are disapproved")