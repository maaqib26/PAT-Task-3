ls = [10,20,30,9]

# Storing the given list into a variable

combination_1 = [ls[0],ls[1],ls[2]]
combination_2 = [ls[0],ls[2],ls[3]]
combination_3 = [ls[0],ls[3],ls[1]]
combination_4 = [ls[1],ls[2],ls[3]]

# Finding out the possible triplet combinations out of the list and storing each triplet into a seperate list variable

if combination_1[0]+combination_1[1]+combination_1[2] == 59:
    print('The Triplet whose sum is equal to 59 are {}'.format(combination_1))
elif combination_2[0]+combination_2[1]+combination_2[2] == 59:
    print('The Triplet whose sum is equal to 59 are {}'.format(combination_2))
elif combination_3[0]+combination_3[1]+combination_3[2] == 59:
    print('The Triplet whose sum is equal to 59 are {}'.format(combination_3))
elif combination_4[0]+combination_4[1]+combination_4[2] == 59:
    print('The Triplet whose sum is equal to 59 are {}'.format(combination_4))

# Verifying with sum of each combination whose sum equals to 59 and printing the same