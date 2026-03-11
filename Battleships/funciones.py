# ==========================================
#  Funciones extras para el juego
# ==========================================

import random, sys
from Variables import LETRAS_COLUMNAS, FILAS, AGUA, IMPACTO, AGUA_DISPARADA


def pedir_coordenadas(tablero_disparos):
    """
    Pide al jugador humano que introduzca coordenadas para disparar.
    Formato esperado: letra + número, por ejemplo "A5" o "J10"
    Valida que:
      - La letra sea válida (A-J)
      - El número sea válido (1-10)
      - No haya disparado ya ahí antes
    Devuelve (fila, columna) como índices numéricos.
    """
    while True:
        entrada = input("Introduce coordenadas para disparar (ej: A5) o escribe 'salir': ").strip().upper()
        if entrada == 'SALIR':
            print('\n👋 Gracias por jugar. ¡Hasta la próxima!')
            raise SystemExit

        # Comprobar formato mínimo: al menos 2 caracteres
        if len(entrada) < 2:
            print("  ❌ Formato incorrecto. Escribe letra + número, ej: B3")
            continue

        letra = entrada[0]           # Primera parte: letra de columna
        numero = entrada[1:]         # Resto: número de fila

        # Comprobar que la letra es válida
        if letra not in LETRAS_COLUMNAS:
            print(f"  ❌ Letra no válida. Usa una de: {', '.join(LETRAS_COLUMNAS)}")
            continue

        # Comprobar que el número es un entero válido
        if not numero.isdigit():
            print("  ❌ El número de fila debe ser un número, ej: A5")
            continue

        fila = int(numero) - 1       # Convertir a índice (1→0, 2→1, ...)
        col = LETRAS_COLUMNAS.index(letra)  # Convertir letra a índice

        # Comprobar que la fila está en rango
        if fila < 0 or fila >= FILAS:
            print(f"  ❌ Fila fuera de rango. Usa números del 1 al {FILAS}")
            continue

        # Comprobar que no ha disparado ya ahí
        if tablero_disparos[fila][col] in [IMPACTO, AGUA_DISPARADA]:
            print("  ❌ Ya has disparado ahí. Elige otra posición.")
            continue

        return fila, col  # Coordenadas válidas


def disparo_maquina(tablero_disparos):
    """
    La máquina elige una posición aleatoria donde no haya disparado antes.
    Devuelve (fila, columna).
    """
    while True:
        fila = random.randint(0, FILAS - 1)
        col = random.randint(0, len(LETRAS_COLUMNAS) - 1)

        # Solo disparar donde no hayamos disparado antes
        if tablero_disparos[fila][col] == AGUA:
            return fila, col


def coordenadas_a_texto(fila, col):
    """
    Convierte coordenadas numéricas a formato legible.
    Ejemplo: (0, 0) → "A1", (2, 4) → "E3"
    """
    letra = LETRAS_COLUMNAS[col]
    numero = fila + 1
    return f"{letra}{numero}"


def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida e instrucciones."""
    print("=" * 50)
    print("      🚢  HUNDIR LA FLOTA  🚢")
    print("=" * 50)
    print()
    print("Instrucciones:")
    print("  - El tablero es de 10x10 (A-J columnas, 1-10 filas)")
    print("  - Para disparar escribe letra + número, ej: B5")
    print("  - X = impacto  |  - = agua  |  ~ = sin disparar")
    print("  - O = tu barco (en tu tablero)")
    print("  - Si aciertas, vuelves a disparar")
    print("  - Gana quien hunda todos los barcos enemigos")
    print()