def sublistZeroSum(given_lst):
    # Iterate through each element of the list
    for i in range(len(given_lst)):
        s = 0  
        # Initialize sum to 0 for each new starting index       
        for j in range(i, len(given_lst)):
            # Iterate through each sublist starting from the current index
            s += given_lst[j]  
            # Add the current element to the sum
            if s == 0: 
                 # If the sum becomes zero, there exists a sublist with zero sum
                return True  
            # Return True if a sublist with zero sum is found
    return False  
# If no sublist with zero sum is found, return False

# Test the function
given_lst = [4, 2, -3, 1, 6]
print(sublistZeroSum(given_lst))  
# Output the result of the function call
