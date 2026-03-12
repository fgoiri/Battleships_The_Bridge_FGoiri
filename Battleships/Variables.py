# ==========================================
# VARIABLES: Constantes del juego
# ==========================================

# Dimensiones del tablero (10x10)
FILAS = 10
COLUMNAS = 10

# Letras para las columnas (como en el juego real: A, B, C...)
LETRAS_COLUMNAS = [' A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# Lo que se muestra en el tablero:
AGUA = '.'           # Casilla vacía (no disparada)
BARCO = 'O'          # Barco (solo visible en tu propio tablero)
IMPACTO = 'X'        # Disparo que ha dado en un barco
AGUA_DISPARADA = '~' # Disparo que ha caído al agua

# Diccionario con los barcos y su eslora (número de casillas que ocupa)
# Nombre del barco -> eslora
BARCOS = {
    'Destructor 1': 1,
    'Destructor 2': 1,
    'Destructor 3': 1,
    'Destructor 4': 1,
    'Crucero 1': 2,
    'Crucero 2': 2,
    'Crucero 3': 2,
    'Acorazado 1': 3,
    'Acorazado 2': 3,
    'Portaaviones': 4,
}

# Orientaciones posibles al colocar un barco
ORIENTACIONES = ['N', 'S', 'E', 'O']