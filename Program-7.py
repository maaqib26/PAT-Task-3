def first_non_repeating_element(lst):
    frequency = {}  
    # Dictionary to store the frequency of each element 
    for num in lst:
        # Count the frequency of each element in the list
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    
    for num in lst:
        # Iterate through the list again to find the first non-repeating element
        if frequency[num] == 1:
            return num  
        # Return the first non-repeating element

    return None  
# Return None if no non-repeating element is found

# Example
given_lst = [4, 2, 5, 2, 4, 6, 6]
result = first_non_repeating_element(given_lst)
if result is not None:
    print("The first non-repeating element is:", result)
else:
    print("No non-repeating element found.")
