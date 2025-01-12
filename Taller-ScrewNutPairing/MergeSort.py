def mergesort(arr):
    if len(arr) <= 1:  # Caso base: una lista vacía o de un solo elemento ya está ordenada
        return arr
    mid = len(arr) // 2  # Dividimos la lista en dos mitades
    left = mergesort(arr[:mid])  # Ordenamos recursivamente la mitad izquierda
    right = mergesort(arr[mid:])  # Ordenamos recursivamente la mitad derecha
    return merge(left, right)  # Combinamos las dos mitades ordenadas

def merge(left, right):
    result = []
    i = j = 0
    # Combinamos las listas ordenadas
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Agregamos los elementos restantes
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [4, 2, 7, 1, 9, 3]
sorted_arr = mergesort(arr)
print("MergeSort:", sorted_arr)
