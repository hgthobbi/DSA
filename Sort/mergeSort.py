def mergeSort(lista):
    if len(lista) == 1:
        return lista
    
    mid = len(lista) // 2
    arrayOne = lista[:mid]
    arrayTwo = lista[mid:]

    arrayOne = mergeSort(arrayOne)
    arrayTwo = mergeSort(arrayTwo)

    return merge(arrayOne, arrayTwo)

def merge(arrayOne, arrayTwo):
    c = []
    while arrayOne and arrayTwo:
        if arrayOne[0] > arrayTwo[0]:
            c.append(arrayTwo[0])
            arrayTwo.remove(arrayTwo[0])
        else:
            c.append(arrayOne[0])
            arrayOne.remove(arrayOne[0])
        
    while arrayOne:
        c.append(arrayOne[0])
        arrayOne.remove(arrayOne[0])
        
    while arrayTwo:
        c.append(arrayTwo[0])
        arrayTwo.remove(arrayTwo[0])

    return c

print(mergeSort([42, 17, 89, 56, 23, 70, 5, 37, 61, 14, 98, 29, 73, 3, 68, 45, 11, 82, 50, 6, 91, 26, 77, 8, 53, 20, 64, 2, 49, 38, 79, 33, 71, 16, 94, 57, 9, 46, 87, 19, 75, 31, 60, 24
]))