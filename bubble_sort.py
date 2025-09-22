def bubble_sort(array,size):
    for i in range(size):
        swaps = 0
        for j in range(0, size-i-1):
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swaps = 1
        if (swaps == 0):
            break

arr = [14,33,27,35,10]
n = len(arr)
print("Array before bubble sort")
print(arr)
bubble_sort(arr,n)
print("Array after bubble sort")
print(arr)