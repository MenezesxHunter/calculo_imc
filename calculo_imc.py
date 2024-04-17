print("####### Cálculo IMC by MenezesXHunter #######")
peso = float(input("Digite o seu Peso em KG: "))
altura = float(input("Digite a sua Altura em Metros: ")) 
imc = peso / altura ** 2

if 17 <= imc <= 24.99:
    print(f" O Seu IMC é :{imc} você está Magro")

elif 25 <= imc <= 29.9:
    print(f" O Seu IMC é :{imc} você está com Sobrepeso")

else:
    print(f" O Seu IMC é :{imc} você está Obeso")
