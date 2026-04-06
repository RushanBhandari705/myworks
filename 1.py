#Write a program that prints out all the elements of a list which are divisible by 2 and 3. Use the following list:
# a = [2,3,6,8,9,12,15,18,24,22,33,112]

a = [2,3,6,8,9,56,46,4,22,33,112]
for i in a:
    if i % 2 == 0 and i % 3 == 0:
        print(i)
