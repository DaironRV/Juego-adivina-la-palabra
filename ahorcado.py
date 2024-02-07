import getpass

palabra_secreta = getpass.getpass("cual palabar quieres ocultar: ").replace(' ', '').lower()

def adivina_palabra(palabra_secreta):
    palabra_oculta = ['_' for _ in palabra_secreta]
    intentos = 0

    while '_' in palabra_oculta and intentos < 12:
        print(' '.join(palabra_oculta))
        letra = input("Ingresa una letra: ").lower()

        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_oculta[i] = letra
        else:
            intentos += 1
            print(f"La letra {letra} no está en la palabra. Has fallado {intentos} veces.")

    if '_' not in palabra_oculta:
        print("¡Felicidades! Has adivinado la palabra.")
    else:
        print("Has alcanzado el límite de intentos. Has fallado.")

adivina_palabra(palabra_secreta)
