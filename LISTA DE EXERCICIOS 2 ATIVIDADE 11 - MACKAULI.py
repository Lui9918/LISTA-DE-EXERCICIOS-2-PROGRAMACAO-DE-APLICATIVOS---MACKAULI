#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

if __name__ == '__main__':
# Entrada do salario
salario_antigo = float(input("Digite o salario do colaborador: "))

# Se o salário for até 280
if (salario_antigo <= 280):
print("20%")
aumento = salario_antigo*0.20
salario_novo = salario_antigo + aumento

elif (salario_antigo > 280) and (salario_antigo <= 700):
print("15%")
aumento = salario_antigo*0.15
salario_novo = salario_antigo + aumento

elif (salario_antigo > 700) and (salario_antigo <= 1500):
print("10%")
aumento = salario_antigo*0.1
salario_novo = salario_antigo + aumento

else:
print("5%")
aumento = salario_antigo*0.05
salario_novo = salario_antigo + aumento

print(f"Aumento: {aumento}")
print(f"Novo salário: {salario_novo}")
