# Necesito tu ayuda para crear un juego de rock, scissors y paper. por consola, el usuario debe ingresar su elección y la computadora debe elegir una respuesta aleatoria. Al final se debe mostrar el resultado del juego.
# Rock gana a scissors
# Scissors gana a paper
# Paper gana a rock
# Si el usuario ingresa una opción inválida, debe mostrar un mensaje de error.

import random
def game():
    user = input("Ingrese su elección: ").lower()
    computer = random.choice(["rock", "scissors", "paper"])
    print(f"Computadora: {computer}")

    if user == computer:
        print("Empate")
    elif user == "rock" and computer == "scissors":
        print("Ganaste")
        return 1
    elif user == "scissors" and computer == "paper":
        print("Ganaste")
        return 1
    elif user == "paper" and computer == "rock":
        print("Ganaste")
        return 1
    elif user == "scissors" and computer == "rock":
        print("Perdiste")
        return -1
    elif user == "paper" and computer == "scissors":
        print("Perdiste")
        return -1
    elif user == "rock" and computer == "paper":
        print("Perdiste")
        return -1
    else:
        print("Opción inválida")
        return 0

score = 0
while True:
    result = game()
    if result is not None:
        score += result
    else:
        # Manejar el caso en que result es None, por ejemplo, asignando un valor predeterminado a result
        result = 0
        score += result
    play_again = input("Desea jugar de nuevo? (si/no): ")
    if play_again.lower() != "si":
        break
print(f"Tu puntuación final es: {score}")
print("Gracias por jugar")


