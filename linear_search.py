def linear_search(a,n,key):
    count = 0
    for i in range(n):
        if (a[i] == key):
            print(f"The number is at the position", (i+1))
            count = count + 1
    if (count == 0):
        print("The number is not present in the array")

a = [12,45,56,75,41,8,65]
n = len(a)
key = 45
linear_search(a,n,key)
key = 77
linear_search(a,n,key)
key = 8
linear_search(a,n,key)
key = 75
linear_search(a,n,key)