def most_frequent_element(lst):
    if not lst:
        return None

    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    max_count = -1
    most_frequent = None
    for item, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent = item

    return most_frequent

my_list = [1, 2, 2, 3, 4, 2, 5, 3]
print(most_frequent_element(my_list))
