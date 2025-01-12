def quicksort(arr):
    if len(arr) <= 1:  # Caso base: una lista vacía o de un solo elemento ya está ordenada
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Elegimos el pivote como el elemento central
        left = [x for x in arr if x < pivot]  # Elementos menores que el pivote
        middle = [x for x in arr if x == pivot]  # Elementos iguales al pivote
        right = [x for x in arr if x > pivot]  # Elementos mayores que el pivote
        return quicksort(left) + middle + quicksort(right)

arr = [4, 2, 7, 1, 9, 3]
sorted_arr = quicksort(arr)
print("QuickSort:", sorted_arr)
