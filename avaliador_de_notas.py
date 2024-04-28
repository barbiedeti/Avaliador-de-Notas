import time

print("Bem vinda ao Avaliador de Notas! \n Abaixo será solicitado suas três notas (de 0 a 10), insira-as para \n descobrir sua média e se você foi aprovado ou reprovado.")

nota1 = float(input("Qual foi sua primeira nota?: "))
nota2 = float(input("Qual foi sua segunda nota?: "))
nota3 = float(input("Qual foi sua terceira nota?: "))

print("Um momento, estamos calculamos sua média...")
time.sleep(3)

#Calculo da média e situação
media = round((nota1 + nota2 + nota3) / 3, 1)

print("Sua média é:", media)
if media >= 6:
    print("Situaçao: Aprovado")
else:
    print("Situação: Reprovado")
