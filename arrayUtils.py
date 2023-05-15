# Function to return the set
# of unique pairs in the array
def find_unique_pairs(source_array=[1, 1, 9, 8, 3, 4, 11, 6, 7]):
    # Set to store unique pairs
    unique_pairs = set()
    arr_length = len(source_array)

    # Create all possible pairs
    for i in range(arr_length):
        for j in range(arr_length):
            unique_pairs.add((source_array[i], source_array[j]))

    # Return the set with unique pairs
    print(f'Unique pairs found:  {len(unique_pairs)}')
    return unique_pairs

# Function is return the number
# of unique pairs in the array
def find_unique_pairs_optimized(source_array=[1, 1, 9, 8, 3, 4, 11, 6, 7]):
    unique_pairs = set()

    for i in range(len(source_array)):
        unique_pairs.add(source_array[i])

    print(f'Count of Unique pairs is:  {pow(len(unique_pairs), 2)}')
    return pow(len(unique_pairs), 2)
