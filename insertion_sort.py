def insertion_sort(array,size):
    for i in range(1,size):
        key = array[i]
        j=i
        while (j>0) and (array[j-1]>key):
            array[j] = array[j-1]
            j=j-1
        array[j] = key

n = int(input("Enter the number of elements: "))
arr = []
for k in range(n):
    arr.append(int(input("Enter the numbers: ")))

print("Numbers in the array are: ")
print(arr)
insertion_sort(arr,n)
print("Numbers in the array after insertion sort: ")
print(arr)