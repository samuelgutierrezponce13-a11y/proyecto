import random

words_by_level = {
    "facil": ["gato", "perro", "manzana", "leche", "sol"],
    "medio": ["banano", "escuela", "amigo", "ventana", "amarillo"],
    "dificil": ["tecnologia", "universidad", "informacion", "pronunciacion", "imaginacion"]
}

def jugar_habla_correcto():
    print("Bienvenido a Habla Correcto. El juego para practicar tu pronunciacion en espanol.")
    print("=" * 60)
    
    print("Selecciona un nivel de dificultad:")
    print("1. Facil")
    print("2. Medio")
    print("3. Dificil")
    
    opcion = input("Ingresa el numero o nombre del nivel (facil, medio, dificil): ").strip().lower()
    
    if opcion in ["1", "facil", "fácil"]:
        nivel = "facil"
    elif opcion in ["2", "medio"]:
        nivel = "medio"
    elif opcion in ["3", "dificil", "difícil"]:
        nivel = "dificil"
    else:
        print("Opcion no valida. Por defecto se seleccionara el nivel FACIL.")
        nivel = "facil"
        
    puntuacion = 0
    errores = 0
    max_errores = 3
    
    print("\nHas seleccionado el nivel " + nivel.upper() + ". Comencemos.")
    print("Recuerda: Tienes permitido un maximo de " + str(max_errores) + " errores antes de que termine el juego.\n")
    
    while errores < max_errores:
        palabra_objetivo = random.choice(words_by_level[nivel])
        
        print("Palabra a pronunciar: " + palabra_objetivo.upper())
        
        reconocido = input("Ingresa lo que capto el sistema de reconocimiento de voz: ").strip().lower()
        
        if reconocido == palabra_objetivo:
            puntuacion += 10
            print("Excelente pronunciacion! +10 puntos. Puntuacion actual: " + str(puntuacion) + "\n")
        else:
            errores += 1
            print("Dijiste '" + reconocido + "' en lugar de '" + palabra_objetivo + "'.")
            print("Errores cometidos: " + str(errores) + "/" + str(max_errores) + ". Puntuacion actual: " + str(puntuacion) + "\n")
            
        if errores < max_errores:
            continuar = input("Deseas intentar con otra palabra? (s/n): ").strip().lower()
            if continuar != 's':
                break
                
    print("\n" + "=" * 60)
    print("JUEGO TERMINADO")
    print("Puntuacion final: " + str(puntuacion) + " puntos.")

if __name__ == "__main__":
    jugar_habla_correcto()
