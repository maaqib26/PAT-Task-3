def is_happy(num):
    seen = set()  
    # Set to store seen numbers to detect cycles
    while num != 1 and num not in seen:  
        # Continue loop until num becomes 1 (happy) or enters a cycle
        seen.add(num)  
        # Add current num to the set of seen numbers
        num = sum(int(digit) ** 2 for digit in str(num))
        # Calculate the sum of the squares of digits of num
    return num == 1  
# Return True if num is 1 (happy), False otherwise

# Example usage:
number_list = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = [num for num in number_list if is_happy(num)]  # Filter out happy numbers from the list
print("Happy numbers in the given list:", happy_numbers)  # Print the list of happy numbers