def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # 1. Hash all entries of the array
    # 2. Keys should only be absolute value
    # 3. filter out keys that have the value greater than 1
    hashtable = {}
    # 1
    for num in a:
        if hashtable.get(abs(num)) is not None:
            hashtable[abs(num)] += 1
        else:
            # 2
            hashtable[abs(num)] = 1
    result = [num for num in hashtable if hashtable[num] > 1]
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
