import os
import time

def main():

    while(True):
        os.system('cls||clear')
        print("Menu principal")
        print("Digite uma das opções e pressione a tecla enter.\n")
        print("1 - Calcular Indice de Massa Corporal IMC ")
        print("0 - Sair ")

        option = input("> ")

        if(option == "1"):
            IMCMenu()
        elif(option == "0"):
            break
        else:
            print("Opção inválida! tente novamente")
            time.sleep(3)

        os.system('cls||clear')
    os.system('cls||clear')

def IMCMenu():
    os.system('cls||clear')
    print("Calculo do Indice de Massa Coporal IMC [<]\n")

    weight = float(input("Digite o seu peso(kg): "))
    height = float(input("Digite a sua altura(m): "))

    imc = CalculateIMC(weight, height)
    imcCondition = GetIMCCondition(imc)

    print(f"\nSeu IMC é: {round(imc,2)}", )
    print(f"Condição: {imcCondition}\n")

    input("Pressione enter para voltar ao menu principal.")

def CalculateIMC(weight, height):
    return weight / height**2


def GetIMCCondition(imc):
    if(imc < 17):
        return "Muito abaixo do peso."    
    elif(imc >= 17 and imc <= 18.49):
        return "Abaixo do peso."
    elif(imc >= 18.50 and imc <= 24.99):
        return "Peso normal."  
    elif(imc >= 25 or imc <= 29.99):
        return "Acima do peso."
    elif(imc >= 30 or imc <= 34.99):
        return "Obsidade I."
    elif(imc >= 35 or imc <= 39.99):
        return "Obsidade II(Severa)."
    elif(imc >= 40):
        return "Obsidade III(Mórbida)."

main()