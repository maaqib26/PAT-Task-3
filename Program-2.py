ls = [10,501,22,37,100,999,87,351]
# Creating a variable with the given list

prime_ls = []
# Creating a empty list to store prime numbers from the given list

for num in ls:
    # Iterating through each element of the list
    for i in range(2,num):
        if num % i == 0:
            # Verifying if there is a factor found by dividing each element from range of 2 to num-1
            break
            # If a factor is found within the given range break from the loop
        else:
            if num not in prime_ls:
                # If no factor is found with the given range and the element is not in prime_ls list, append the found prime no. to prime_ls
                prime_ls.append(num)
print('The prime numbers found in the given list {} are as follows {}'.format(ls,prime_ls))




