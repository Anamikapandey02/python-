#program to find the sum of a list
#ishan hambir

total = 0
 
# creating a list

list1 = [11, 5, 17, 18, 23]
 

for ele in range(0, len(list1)):

    total = total + list1[ele]
 
# printing total value

print("Sum of all elements in given list: ", total)