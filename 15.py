#Write a program to store the values of the matrix given below in a 2D list. Then calculate the sum of the
#diagonal elements, the sum of all elements above the diagonal and the sum of all elements above the diagonal, and the
#sum of all the elements below the diagonal. Also find out the max and min element from the matrix.


#A = [[1, 2, 3],
 #    [8, 9, 4],
 #    [7, 6, 5]]

#B = [[2, 7, 6],
 #    [9, 5, 1],
 #    [4, 3, 8]]

A = [[1, 2, 3],
     [8, 9, 4],
     [7, 6, 5]]

diagonal_sum = 0
above_diagonal_sum = 0
below_diagonal_sum = 0
max_element = A[0][0]    

for i in range(len(A)):
    for j in range(len(A[i])):
        if i == j:
            diagonal_sum += A[i][j]
        elif i < j:
            above_diagonal_sum += A[i][j]
        else:
            below_diagonal_sum += A[i][j]
        
        if A[i][j] > max_element:
            max_element = A[i][j]

min_element = A[0][0]
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j] < min_element:
            min_element = A[i][j]

print("Sum of diagonal elements:", diagonal_sum)
print("Sum of elements above the diagonal:", above_diagonal_sum)
print("Sum of elements below the diagonal:", below_diagonal_sum)
print("Maximum element in the matrix:", max_element)
print("Minimum element in the matrix:", min_element)






 


