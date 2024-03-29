def min_difference_mangoes(bags, students):
    bags.sort()  
    # Sort bags in ascending order of mangoes
    min_difference = float('inf') 
     # Initialize minimum difference to positive infinity

    # Iterate through the bags and use a sliding window approach to find the minimum difference
    for i in range(len(bags) - students + 1):
        # Calculate the mangoes in the bag with maximum mangoes and the bag with minimum mangoes given to a student
        max_mangoes_bag = bags[i + students - 1]
        min_mangoes_bag = bags[i]
        difference = max_mangoes_bag - min_mangoes_bag
        # Update the minimum difference if a smaller difference is found
        min_difference = min(min_difference, difference)

    return min_difference

# Example usage:
bags = [3, 7, 2, 5, 8, 4]  # List of mangoes in each bag
students = 3  
# Number of students
min_difference = min_difference_mangoes(bags, students)
print("Minimum difference between maximum and minimum mangoes given to a student:", min_difference)
