import random

elecciones = ["piedra","papel","tijera"]

def eleccion_maquina():
    return random.choice(elecciones)

def eleccion_jugador():
    eleccion = input("Elige: piedra, papel o tijera: ").lower()
    return eleccion
    
def ganador(eleccion, eleccion_maquina):
    if eleccion == eleccion_maquina:
        return "¡Es un empate!"
    elif (
        (eleccion == "piedra" and eleccion_maquina == "tijera") or
        (eleccion == "papel" and eleccion_maquina == "piedra") or
        (eleccion == "tijera" and eleccion_maquina == "papel")
        ):
        return "¡Ganaste!"
    else:
        return "Perdiste. La máquina ganó."

def juego():
    maquina = eleccion_maquina()
    jugador = eleccion_jugador()
    print(f"La máquina eligió: {maquina}")
    print(f"Tú elegiste: {jugador}")
    print(ganador(jugador, maquina))

juego()