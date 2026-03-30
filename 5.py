#Write a program that contains two lists of equal length and alternatingly taking elements. eg
# ['a','b','c'], [1,2,3] -> ['a',1,'b',2,'c',3]

list1 = ['a','b','c','d']
list2 = [1,2,3,4]
new_list = []
for i in range(len(list1)):
    new_list.append(list1[i])
    new_list.append(list2[i])
print(new_list)

