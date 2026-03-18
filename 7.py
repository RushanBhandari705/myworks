#Write a program that performs element-wise addition of two lists of numbers having the same length and outputs another list containing the sums.
# [1,2,3,4,5,6] + [1,2,3,4,5,6] -> [2,4,6,8,10,12]
list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i] + list2[i])
print(new_list)

