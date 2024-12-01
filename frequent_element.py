#Develop a function that finds the most frequent element in a list.

def most_frequent_element(lst):
    if not lst:  # Check if the list is empty
        return None

    # Create a dictionary to store frequencies
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    # Find the element with the maximum frequency
    max_count = -1
    most_frequent = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = item

    return most_frequent

# Example usage:
my_list = [1, 2, 2, 3, 4, 2, 5, 3]
print(most_frequent_element(my_list))  # Output: 2
