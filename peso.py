import math

nombre = input("como te llamas? ")
print (nombre) 



genero = input("¿Cuál es tu género?: ")
while genero.lower() not in ["hombre", "mujer"]:
    print("Solo existen dos géneros, hombre y mujer.")
    genero = input("¿Cuál es tu género?: ") 


calculoPeso = float(input("dime tu peso: "))
calculoAltura = float(input("dime tu altura: "))

calculoCarboidratos = float(input("dime cuantos carboidratos haz comido (en gramos): "))
calculoProteinar = float(input("dime cuantos gramos de proteina haz comido: "))
calculoGrasas = float(input("dime cuantos gramos de grasas haz comido: "))
cintura = float(input("te puedes medir y decirme cuanto tienes de cintura: ")) 

resultadoGrasaMujer = (cintura/(calculoAltura*math.sqrt(calculoAltura))-18)/calculoAltura
resultadoGrasaHombre = (calculoPeso-(calculoPeso*0.85) + 28 - (cintura*0.35))/calculoPeso*100 
resultado = calculoPeso / (calculoAltura**2)
print("tu indice de masa corporal es de: ", resultado)
resultado2 = (calculoCarboidratos*4)+(calculoProteinar*4)+(calculoGrasas*9)
print("haz consumido: ", resultado2, "calorias")

# esta funciona como un buen ejempl de mantener algo en un rago establecido
if 18.5 <= resultado < 24:
    print("Tu índice de masa corporal es sano")
else:
    print("Tu índice de masa corporal no es sano")


if genero == "hombre" or genero == "Hombre":
    print("tu porcentaje de grasa es: ", resultadoGrasaHombre, "%")
    if 11 <= resultadoGrasaHombre <22:
        print("Tienes un posentaje de grasa saludable")
    elif resultadoGrasaHombre < 11:
        print("tienes que aumentar tu porcentaje de grasa")
    elif resultadoGrasaHombre >22:
        print("tienes que bajar tu procentaje de grasa")
        
elif genero == "mujer" or genero == "Mujer": 
    print("tu porcentaje de grasa es : ", resultadoGrasaMujer,"%")
    if 11 <= resultadoGrasaMujer <22:
        print("Tienes un posentaje de grasa saludable")
    elif resultadoGrasaMujer < 11:
        print("tienes que aumentar tu porcentaje de grasa")
    elif resultadoGrasaMujer >22:
        print("tienes que bajar tu procentaje de grasa")