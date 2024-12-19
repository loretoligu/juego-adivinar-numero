from random import randint

number = randint(1, 100)
tries = 0

name = input("¿Cómo te llamas? ")
print(f"Hola {name}, he pensado un número del 1 al 100 y tienes 8 intentos para averiguar cuál es\n")

while tries < 8:
    print(f"Te quedan {8-tries} intentos\n")
    guess = int(input("Introduce el número: "))
    tries += 1

    if(guess < 1) | (guess > 100):
        print("El número no se encuentra en el rango indicado")
    else:
        if guess < number:
            print(f"{guess} es menor que el número")
        elif guess > number:
            print(f"{guess} es mayor que el número")
        else:
            print(f"Enhorabuna {name}, has adivinado el numero en {tries} intentos")
            break

if tries >= 8:
    print(f"Qué lástima, se te han acabado los intentos. El numero era {number}")
