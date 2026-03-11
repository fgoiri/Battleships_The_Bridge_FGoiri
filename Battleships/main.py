# ==========================================
# MAIN Programa principal
# ==========================================

from Clase_Tablero import Tablero
from funciones import (pedir_coordenadas, disparo_maquina,
                       coordenadas_a_texto, mostrar_bienvenida)


def main():
    # --- BIENVENIDA ---
    mostrar_bienvenida()

    # --- INICIALIZAR TABLEROS ---
    # Creamos un tablero para el jugador y otro para la máquina
    # Al crear el tablero, los barcos se colocan automáticamente
    tablero_jugador = Tablero('Jugador')
    tablero_maquina = Tablero('Máquina')

    print("¡Los barcos han sido colocados! ¡Que empiece la batalla!\n")

    # --- BUCLE PRINCIPAL DEL JUEGO ---
    turno_jugador = True  # El jugador empieza primero

    while True:

        # ==================
        # TURNO DEL JUGADOR
        # ==================
        if turno_jugador:
            print("\n" + "=" * 50)
            print("  🎯 TU TURNO")
            print("=" * 50)

            # Mostrar tablero propio (con tus barcos) y tus disparos
            tablero_jugador.imprimir_tablero_propio()
            tablero_jugador.imprimir_tablero_disparos()

            # Pedir coordenadas al jugador
            resultado = pedir_coordenadas(tablero_jugador.tablero_disparos)
            if resultado is None:
                break
            fila, col = resultado
            coord_texto = coordenadas_a_texto(fila, col)

            # Comprobar si hay impacto en el tablero de la máquina
            impacto = tablero_maquina.recibir_disparo(fila, col)

            # Actualizar nuestro tablero de disparos
            tablero_jugador.marcar_disparo_propio(fila, col, impacto)

            if isinstance(impacto, str) and impacto.startswith("Hundido"):
                print(f"\n  🔥 ¡HUNDIDO en {coord_texto}! ¡Vuelves a disparar!")
                turno_jugador = True
            elif impacto:
                print(f"\n  💥 ¡IMPACTO en {coord_texto}! ¡Vuelves a disparar!")
                turno_jugador = True
            else:
                print(f"\n  💧 Agua en {coord_texto}. Turno de la máquina.")
                turno_jugador = False

            # Comprobar si el jugador ha ganado
            if not tablero_maquina.tiene_barcos():
                print("\n" + "🏆" * 20)
                print("  ¡¡¡ENHORABUENA!!! ¡Has ganado!")
                print("🏆" * 20)
                break

        # ==================
        # TURNO DE LA MÁQUINA
        # ==================
        else:
            print("\n" + "=" * 50)
            print("  🤖 TURNO DE LA MÁQUINA")
            print("=" * 50)

            fila, col = disparo_maquina(tablero_maquina.tablero_disparos) # La máquina elige dónde disparar
            coord_texto = coordenadas_a_texto(fila, col)
            print(f"  La máquina dispara a {coord_texto}...")

            resultado = tablero_jugador.recibir_disparo(fila, col)
            tablero_maquina.marcar_disparo_propio(fila, col, resultado)

            if isinstance(resultado, str) and resultado.startswith("Hundido"):
                print(f"  💥 ¡La máquina ha hundido un barco en {coord_texto}! Repite turno.")
                turno_jugador = False
        
            elif resultado:
                print(f"  💥 ¡La máquina ha impactado en {coord_texto}! Repite turno.")
                turno_jugador = False
        
            else:
                print(f"  💧 La máquina ha fallado en {coord_texto}.")
                turno_jugador = True

            if not tablero_jugador.tiene_barcos():
                print("\n" + "💀" * 20)
                print("  La máquina ha ganado. ¡Mejor suerte la próxima vez!")
                print("💀" * 20)
                break
            
# Punto de entrada del programa
if __name__ == '__main__':
    main()