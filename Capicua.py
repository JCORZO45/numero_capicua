# Quiz leer numero entero de 5 digitos y determinar si es capicua 


print("--------------------------")
print("------Numero-capicua------")
print("--------------------------")

#input 
n=input("Digite el numero: ")
n=int(n)

#process 
c1 = n//10000
if 0<c1<10: 
    c2= ((n%10000)-(n%1000))//1000

    c5=n%10

    c4=((n%100)-(n%10))//10

    print("")
    if c1==c5 and c2==c4:
        print("El numero es capicua")
    else:
        print("No es un numero capicua ")
        
        
else: 
    print("EL numero ingresado no es de 5 cifras, porfavor digite un nuevo numero")

#output 
print("-----RESULTADOS------")
