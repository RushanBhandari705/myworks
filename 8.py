#Given two lists of alphabets of equal length, perform element wise concat and store the result in a new list.
#['a','b','c','d','e'] + ['f','g','h','i','j'] -> ['af','bg','ch','di','ej']
list1 = ['a','b','c','d','e']
list2 = ['f','g','h','i','j']
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i] + list2[i])
print(new_list)