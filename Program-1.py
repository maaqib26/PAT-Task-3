l = [10,501,22,37,100,999,87,351]
# Storing the given list in a variable 'l'
l_even = []
# Initializing an empty list to store all even elements
l_odd = []
# Initializing an empty list to store all odd elements
for i in l:
    # Iterating through the each element of list 'l'
    if i%2 == 0:
        l_even.append(i)
        # If mod of each element equal to 0 append those elements to 'l_even' list
    elif i%2 != 0:
        l_odd.append(i)
        # If mod of each element not equal to 0 append those elements to 'l_odd' list

print('The even elements in the given list {} are as follows {}'.format(l,l_even))
# Printing Even elements from the given list
print('The odd elements in the given list {} are as follows {}'.format(l,l_odd))
# Printing Even elements from the given list