import random
import time
import os

def borrarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def siAvanza():
    return random.randint(0, 1) == 0

def mostrarCarrera(busUno, busDos):
    carril1A = list(" " * 30)
    carril1B = list(" " * 30)
    carril1C = list(" " * 30)
    carril1D = list(" " * 30)  
    
    carril2A = list(" " * 30)
    carril2B = list(" " * 30)
    carril2C = list(" " * 30)
    carril2D = list(" " * 30)  
    
    if busUno <= 29:  
        carril1A[busUno] = "----------     "  
        carril1B[busUno] = "|        |---- "
        carril1C[busUno] = "|Juanjo       |"
        carril1D[busUno] = "---0------0--- "
    
    if busDos <= 29:  
        carril2A[busDos] = "----------     "  
        carril2B[busDos] = "|        |---- "
        carril2C[busDos] = "|Brahian      |"
        carril2D[busDos] = "---0------0--- " 
    print()
    print("//////////////////////////////////////////// META")
    print()
    print("".join(carril1A))
    print("".join(carril1B))
    print("".join(carril1C))
    print("".join(carril1D))
    print()
    print("//////////////////////////////////////////// META")
    print("//////////////////////////////////////////// META")
    print()
    print("".join(carril2A))
    print("".join(carril2B))
    print("".join(carril2C))
    print("".join(carril2D))
    print()
    print("//////////////////////////////////////////// META")

def carrera():
    alguienGana = False
    busUno = 0
    busDos = 0
    
    while not alguienGana:
        borrarPantalla()
        
        # Turno del Bus 1
        if siAvanza():
            busUno += 1
        
        mostrarCarrera(busUno, busDos)
        time.sleep(0.08)
        
        if busUno == 29:
            alguienGana = True
            print("¡Juanjo Gana!")
            break
        
        borrarPantalla()
        
        # Turno del Bus 2
        if siAvanza():
            busDos += 1
            
        mostrarCarrera(busUno, busDos)
        time.sleep(0.08)
        
        if busDos == 29:
            alguienGana = True
            print("¡Brahian Gana!")
            break

# Ejecutar la carrera
carrera()