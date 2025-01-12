def emparejar_tornillos_y_tuercas(tornillos, tuercas):
    """Función principal para emparejar tornillos y tuercas."""
    def particionar(arreglo, bajo, alto, pivote):
        """Particiona el arreglo según el pivote."""
        i = bajo
        for j in range(bajo, alto):
            if arreglo[j] < pivote:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
                i += 1
            elif arreglo[j] == pivote:
                arreglo[j], arreglo[alto] = arreglo[alto], arreglo[j]
                j -= 1
        arreglo[i], arreglo[alto] = arreglo[alto], arreglo[i]
        return i

    def emparejar_recursivo(tornillos, tuercas, bajo, alto):
        """Función recursiva para emparejar tornillos y tuercas."""
        if bajo < alto:
            print(f"\nTornillos actuales: {tornillos[bajo:alto+1]}")
            print(f"Tuercas actuales:   {tuercas[bajo:alto+1]}")

            # Usar el primer tornillo como pivote para particionar las tuercas
            pivote_tornillo = tornillos[bajo]
            indice_pivote = particionar(tuercas, bajo, alto, pivote_tornillo)
            print(f"Tornillo {pivote_tornillo} emparejado con tuerca {tuercas[indice_pivote]}")

            # Usar la tuerca emparejada como pivote para particionar los tornillos
            pivote_tuerca = tuercas[indice_pivote]
            particionar(tornillos, bajo, alto, pivote_tuerca)

            # Llamar recursivamente en las sublistas izquierda y derecha
            emparejar_recursivo(tornillos, tuercas, bajo, indice_pivote - 1)
            emparejar_recursivo(tornillos, tuercas, indice_pivote + 1, alto)

    print("Tornillos y tuercas iniciales:")
    print(f"Tornillos: {tornillos}")
    print(f"Tuercas:   {tuercas}\n")
    emparejar_recursivo(tornillos, tuercas, 0, len(tornillos) - 1)

    print("\nEmparejamiento final:")
    for i in range(len(tornillos)):
        print(f"Tornillo {tornillos[i]} ↔ Tuerca {tuercas[i]}")

# Ejemplo de ejecución
tornillos = [4, 2, 6, 1, 5, 3]
tuercas = [3, 5, 1, 6, 2, 4]
emparejar_tornillos_y_tuercas(tornillos, tuercas)
