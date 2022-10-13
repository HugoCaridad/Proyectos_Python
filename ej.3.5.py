import random

numrandom = random.randint(1,20)

print("Vas a adivinar un numero entre el 1 y 100, pero solo tienes 3 vidas")

oportunidades=3
while(oportunidades>0):
    numusuario= int(input("Dime un num: "))
    if(numusuario!=numrandom):
        oportunidades=oportunidades-1
        if(oportunidades!=1):
            print("Te quedan",oportunidades,"vidas")
        else:
            print("Te quedan",oportunidades,"vidas")
    else:
        print("Has acertado el número")
        break


if (oportunidades==0):
    print("El num era:",numrandom)