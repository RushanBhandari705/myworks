list1 = [1,2,3,4,5,6]
list2 = [1,3,4,5,6,7]
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i] + list2[i])
print(new_list)

