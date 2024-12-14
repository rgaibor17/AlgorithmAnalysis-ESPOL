
def busqueda_secuencial_texto(texto, patron):
    n = len(texto)
    m = len(patron)
    ocurrencias = []

    print(f"Texto: '{texto}'")
    print(f"Patron: '{patron}'")
    print("\nComenzando Prueba...\n")

    for i in range(n - m + 1):
        print(f"Verificando indice {i}...")
        j = 0
        while j < m and texto[i + j] == patron[j]:
            print(f"  texto[{i + j}] == patron[{j}] -> '{texto[i + j]}' == '{patron[j]}'")
            j += 1
        if j == m:
            print(f"  Patron encontrado en indice {i}\n")
            ocurrencias.append(i)
        if j < m:
            print(f"  Error: texto[{i + j}] != patron[{j}] -> '{texto[i + j]}' != '{patron[j]}'\n")
    
    if not ocurrencias:
        print("Patron no encontrado\n")
    return ocurrencias


#Tests
texto = input("Ingresar texto: ")
patron = input("Ingresar patron a buscar: ")

result = busqueda_secuencial_texto(texto, patron)
if result:
    print(f"Resultado: Patron encontrado en indice(s) {result}")
else:
    print("Resultado: Patron no encontrado")
