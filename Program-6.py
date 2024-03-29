l1 = [2,3,6,5,7]
l2 = [2,78,3,46,00,99]
l3 = [111,333,2,333,111,3,777,777]
# Defining 3 list which has common elements within them

common = list(filter(lambda x: x in l2 and x in l3, l1))
#Creating a lambda expression and filtering out the common elements between the given 3 lists
print('The Command elements in the given 3 list \n{}\n{}\n{}\nare {}'.format(l1,l2,l3,common))
# printing the common elements found in the 3 list