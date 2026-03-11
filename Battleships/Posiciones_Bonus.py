def pedir_posicion_barco(nombre, eslora, tablero_propio):
    """El jugador elige dónde colocar un barco. Ej: B5 N"""
    while True:
        print(f"\n  Coloca el {nombre} (eslora {eslora})")
        entrada = input("  Posición + orientación (ej: B5 N): ").upper().split()

        if len(entrada) != 2:
            print("  ❌ Escribe posición y orientación, ej: B5 N")
            continue

        coordenada, orientacion = entrada
        letra = coordenada[0]
        numero = coordenada[1:]

        if (letra not in LETRAS_COLUMNAS or not numero.isdigit()
                or orientacion not in ORIENTACIONES):
            print("  ❌ Formato incorrecto")
            continue

        fila = int(numero) - 1
        col = LETRAS_COLUMNAS.index(letra)
        return fila, col, orientacion