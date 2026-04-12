
list1 = ['a','b','c','d','e']
list2 = ['f','g','h','i','j']
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i] + list2[i])
print(new_list)
