def insertion_sort(array,size):
    for i in range(size):
        imin = i
        for j in range(i+1,size):
            if array[j] < array[imin]:
                imin = j
        temp = array[i]
        array[i] = array[imin]
        array[imin] = temp

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))
    
print("Numbers in the array are:")
print(arr)
n = len(arr)
print("Array before selection sort")
print(arr)
insertion_sort(arr,n)
print("Array after selection sort")
print(arr)