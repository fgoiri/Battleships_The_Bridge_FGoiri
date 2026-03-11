import random
from Variables import (FILAS, COLUMNAS, LETRAS_COLUMNAS,
                       AGUA, BARCO, IMPACTO, AGUA_DISPARADA,
                       BARCOS, ORIENTACIONES)


class Tablero:
    """
    Esta clase representa el tablero del jugador.
    Cada jugador tiene:
      - tablero_propio: su tablero con sus barcos (lo ve él)
      - tablero_disparos: lo que ha disparado la máquina (lo ve él)
    """

    def __init__(self, id_jugador):
        """
        Inicializa el tablero vacío y coloca los barcos.
        id_jugador: 'jugador' o 'maquina'
        """
        self.id_jugador = id_jugador

        # Tablero propio: matriz 10x10 llena de AGUA
        # Aquí se verán los barcos y los impactos recibidos
        self.tablero_propio = [[AGUA] * COLUMNAS for _ in range(FILAS)]

        # Tablero de disparos: lo que hemos disparado al enemigo
        # Solo muestra AGUA_DISPARADA e IMPACTO (no los barcos enemigos)
        self.tablero_disparos = [[AGUA] * COLUMNAS for _ in range(FILAS)]

        # Lista de coordenadas donde hay barcos (para comprobar impactos)
        # Ejemplo: [(0,0), (0,1), (3,5), ...]
        # Lista de barcos con sus coordenadas para saber cuándo se hunden
        self.coordenadas_barcos = []
        self.barcos = []

        # Colocar los barcos al inicializar
        self.inicializar_tablero()

    # ------------------------------------------
    # INICIALIZACIÓN: colocar barcos
    # ------------------------------------------

    def inicializar_tablero(self):
        """Coloca todos los barcos del diccionario BARCOS de forma aleatoria."""
        for nombre_barco, eslora in BARCOS.items():
            self._colocar_barco(nombre_barco, eslora)

    def _colocar_barco(self, nombre, eslora):
        """
        Coloca un barco de forma aleatoria en el tablero.
        Elige posición y orientación al azar hasta encontrar una válida.
        """
        colocado = False
        while not colocado:
            # Elegir fila, columna y orientación al azar
            fila = random.randint(0, FILAS - 1)
            col = random.randint(0, COLUMNAS - 1)
            orientacion = random.choice(ORIENTACIONES)

            # Calcular las casillas que ocuparía el barco
            casillas = self._calcular_casillas(fila, col, eslora, orientacion)

            # Si las casillas son válidas, colocar el barco
            if casillas and self._casillas_libres(casillas):
                for (f, c) in casillas:
                    self.tablero_propio[f][c] = BARCO
                    self.coordenadas_barcos.append((f, c))
                self.barcos.append(casillas) # Guardamos las coordenadas de cada barco para saber cuándo se hunden
                colocado = True

    def _calcular_casillas(self, fila, col, eslora, orientacion):
        """
        Calcula las casillas que ocuparía un barco dada su posición,
        eslora y orientación.
        Devuelve una lista de tuplas (fila, col) o [] si se sale del tablero.

        Orientaciones:
          N = hacia arriba    (fila disminuye)
          S = hacia abajo     (fila aumenta)
          E = hacia la derecha (col aumenta)
          O = hacia la izquierda (col disminuye)
        """
        casillas = []
        for i in range(eslora):
            if orientacion == 'N':
                f, c = fila - i, col
            elif orientacion == 'S':
                f, c = fila + i, col
            elif orientacion == 'E':
                f, c = fila, col + i
            elif orientacion == 'O':
                f, c = fila, col - i

            # Comprobar que no se sale del tablero
            if f < 0 or f >= FILAS or c < 0 or c >= COLUMNAS:
                return []  # Fuera del tablero, posición no válida
            casillas.append((f, c))

        return casillas

    def _casillas_libres(self, casillas):
        """
        Comprueba que todas las casillas estén vacías (AGUA).
        Así evitamos poner un barco encima de otro.
        """
        for (f, c) in casillas:
            if self.tablero_propio[f][c] != AGUA:
                return False
        return True
    
    # ------------------------------------------
    # DISPARO: comprobar si hay impacto
    # ------------------------------------------

    def recibir_disparo(self, fila, col):
        """
        Comprueba si el disparo en (fila, col) impacta en un barco.
        Actualiza el tablero_propio con IMPACTO o AGUA_DISPARADA.
        Devuelve True si hay impacto, False si es agua.
        Además comprueba si el barco se ha hundido y devuelve "Hundido X casillas" si es el caso.
        """
        
        if (fila, col) in self.coordenadas_barcos:
            self.tablero_propio[fila][col] = IMPACTO
            
            # comprobar si el barco se ha hundido
            for barco in self.barcos:
                if (fila, col) in barco:
                    hundido = True

                    for f, c in barco:
                        if self.tablero_propio[f][c] != IMPACTO:
                            hundido = False
                            break

                    if hundido:
                        return "Hundido " + str(len(barco)) + " casillas"

            return True  # ¡Impacto!
    
        else:
            self.tablero_propio[fila][col] = AGUA_DISPARADA
            return False  # Agua

    def marcar_disparo_propio(self, fila, col, impacto):
        """
        Actualiza nuestro tablero de disparos para recordar
        dónde hemos disparado y si fue impacto o agua.
        """
        if impacto:
            self.tablero_disparos[fila][col] = IMPACTO
        else:
            self.tablero_disparos[fila][col] = AGUA_DISPARADA

    def tiene_barcos(self):
        """
        Comprueba si al jugador le quedan barcos sin hundir.
        Devuelve True si quedan barcos, False si todos están hundidos.
        """
        for fila in self.tablero_propio:
            if BARCO in fila:
                return True
        return False

    # ------------------------------------------
    # IMPRIMIR TABLERO
    # ------------------------------------------

    def imprimir_tablero_propio(self):
        """Imprime el tablero propio (con tus barcos visibles)."""
        print(f"\n  Tablero de {self.id_jugador}:")
        self._imprimir_matriz(self.tablero_propio)

    def imprimir_tablero_disparos(self):
        """Imprime el tablero de disparos (lo que has disparado al enemigo)."""
        print(f"\n  Disparos de {self.id_jugador} al enemigo:")
        self._imprimir_matriz(self.tablero_disparos)

    def _imprimir_matriz(self, matriz):
        """
        Función auxiliar que imprime cualquier matriz 10x10
        con letras en las columnas y números en las filas.
        """
        # Cabecera con las letras (columnas)
        print("    " + "  ".join(LETRAS_COLUMNAS))
        print("   " + "---" * COLUMNAS)

        # Filas numeradas del 1 al 10
        for i, fila in enumerate(matriz):
            numero = str(i + 1).rjust(2)  # "1", "2"... " 1", " 2" (alineado)
            print(f" {numero}| " + "  ".join(fila))
            