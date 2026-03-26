n = int(input("Enter No elements: "))
arr = list(map(int, input("Enter elements: ").split()))
for i in range(0,n-1,2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print("Array after swapping adjacent elements:", *arr)