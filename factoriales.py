import time

# Hacer factores

def factorial_while(num):
    index = num
    res=1
    while(index>0):
       res = res *index
       index= index -1
    return res
      
num= int(input("Dime un número: "))
print("El factorial del número ",num," es:" ,factorial_while(num))



def factorial_for(num):
    res=1
    for i in range(1,num+1):
       res = res * i
    return res
num= int(input("Dime un número: "))
print("El factorial del número ",num," es:" ,factorial_for(num))


# Dado un numero eliminar su primer digito
"""
num= str(input("Dime un número: "))
tam=len(num)
res=""
for i in range(1,tam):
   res+= num[i]
print("El factorial del número ",num," es:" ,res)
"""
def factorial_rec(n):
    if(n==1):
        return 1
    elif(n==0):
        return 1
    else:
        return n*factorial_rec(n-1)


n= int(input("Dime un número: "))
print(factorial_rec(num))


inicio= time.time()
factorial_while(30)
fin= time.time()
total= fin-inicio
print("El programa Factorial con while ha tardado",total,"segundos")

inicio= time.time()
factorial_for(30)
fin= time.time()
total= fin-inicio
print("El programa Factorial con for ha tardado",total,"segundos")

inicio= time.time()
factorial_rec(30)
fin= time.time()
total= fin-inicio
print("El programa Factorial con recursividad ha tardado",total,"segundos")