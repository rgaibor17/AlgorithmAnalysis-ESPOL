def emparejar_tornillos_y_tuercas(tornillos, tuercas, bajo, alto):
    if bajo < alto:
        # Seleccionar un tornillo pivote y particionar las tuercas
        indice_pivote = particionar(tuercas, bajo, alto, tornillos[bajo])
        
        # Emparejar el tornillo pivote con la tuerca pivote
        particionar(tornillos, bajo, alto, tuercas[indice_pivote])
        
        # Aplicar recursivamente en las sublistas
        emparejar_tornillos_y_tuercas(tornillos, tuercas, bajo, indice_pivote - 1)
        emparejar_tornillos_y_tuercas(tornillos, tuercas, indice_pivote + 1, alto)

def particionar(arreglo, bajo, alto, pivote):
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
