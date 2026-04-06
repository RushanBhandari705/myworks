

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

matrix = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        if i == j:
            matrix[i][j] = 1
        elif i < j:
            matrix[i][j] = 2 
        else:
            matrix[i][j] = 3
for row in matrix:
    print(row)
