#write a program that creates a new list containing all the elements placed on even positions of the original list.
# [43,23,21,44,56,75] -> [23,44,75]
original_list = [43,23,44,56,75]
new_list = []
for i in range(1, len(original_list), 2):
    new_list.append(original_list[i])
print(new_list)

