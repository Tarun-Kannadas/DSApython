def shell_sort(array,n):
    gap = n//2
    while gap > 0:
        for i in range(int(gap),n):
            temp = array[i]
            j=i
            while j>=gap and array[j-gap] > temp:
                array[j] = array[j-gap]
                j = j-gap
                array[j] = temp
        gap = gap//2

arr=[4,12,56,25,34,65,78,7]
n = len(arr)
print("Array before sorting: ")
print(arr)
shell_sort(arr,n)
print("Array after sorting: ")
print(arr)