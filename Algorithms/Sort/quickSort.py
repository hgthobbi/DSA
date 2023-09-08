# # recursive alg
# # pivot has to be in correct position in final sorted array, items to left are smaller, items to right are larger

# # stop when index of itemFrom Left is greater than itemFromRight

# def quickSort(array, low, high):
#     if low<high:
#         pivot_location = partition(array, low, high)
#         quickSort(array, low, pivot_location)
#         quickSort(array, pivot_location+1, high)
#     return array

# def partition(array, low, high):
#     pivot = array[low]
#     leftwall = low 

#     for i in range(low+1, high):
#         if array[i] < pivot:
#             temp = array[i]
#             array[leftwall] = array[i]
#             array[i] = temp
#             leftwall+=1

#     temp2 = array[leftwall]
#     array[leftwall] = pivot
#     pivot = temp2
#     #print(array)
#     return leftwall
    
# array = [5, 4, 3, 2, 1]
# low = 0
# high = len(array)
# print(quickSort(array, low, high))

# chat gpt method
def quicksort(arr):
    if len(arr) <= 1:
        return arr  # Base case: an array with 0 or 1 elements is already sorted

    pivot = arr[len(arr) // 2]  # Choose a pivot element (middle element in this example)
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    # Recursively sort the sub-arrays and combine them
    return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)