#Write a program that contains two lists by alternating elements.
# ['A','H','M'], ['@','#','&'] -> ['A','@','H','#','M','&']
list1 = ['A','H','M']
list2 = ['@','#','&']
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i])
    new_list.append(list2[i])
print(new_list)
