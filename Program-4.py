num = 2574
# Storing the given integer into a variable

num_s = str(num)
# Type casting the integer into a string

num_1st = int(num_s[0])
# Storing the 1st digit into a variable and converting it into interger
num_last = int(num_s[-1])
# Storing the last digit into a variable and converting it into interger
sum = num_1st+num_last
# Adding the 1st, last digits and storing it into a variable

print('The sum of the 1st and last digit of the given interger {} is {}'.format(num,sum))
# Printing the sum of 1st and last digit