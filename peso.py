nombre = input("como te llamas? ")
print (nombre) 

calculoPeso = float(input("dime tu peso: "))
calculoAltura = float(input("dime tu altura: "))

resultado = calculoPeso / (calculoAltura**2)
print("tu indice de masa corporal es de: ", resultado)

if 18.5 <= resultado < 24:
    print("Tu índice es sano")
else:
    print("Tu índice no es sano")