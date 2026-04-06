arr = [50,60,70,80]

key = int(input("Enter number to search: "))

for i in range(len(arr)):
    if arr[i] == key:
        print("Found at index", i)
        break
else:
    print("Not found")
