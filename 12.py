arr = [5, 2, 8, 1, 3,6]

n = len(arr)

for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            # swap
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array:", arr)
