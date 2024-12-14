
def busqueda_secuencial_texto(patron, texto):
    m = len(patron)
    n = len(texto)
    ocurrencias = []
    for i in range(n - m + 1):
        j = 0
        while j < m and patron[j] == texto[i + j]:
            j += 1
            if j == m: 
                ocurrencias.append(i) 
    return ocurrencias

# Ejemplo de uso 

patron = "algo"
texto = "hago algo de algoritmos"
resultado = busqueda_secuencial_texto(patron, texto)
print("El patrón se encontró en las siguientes posiciones:", resultado)
