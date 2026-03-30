#Write a program that creates a new list containing all the elements placed on odd positions of the original list.
# [12,22,32,42,52,62] -> [12,32,52]
original_list = [12,22,32,42,52,60]
new_list = []
for i in range(0, len(original_list), 2):
    new_list.append(original_list[i])
print(new_list)

