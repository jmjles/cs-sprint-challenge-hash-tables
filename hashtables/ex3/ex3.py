def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # 1. hash first array
    # 2. Check if next array containes any from the first array
    # 3. Remove hash values that has a count of one
    # 4. Repeat check and remove untill all arrays have been checked
    result = []
    hashtable = {}
    if len(arrays) <= 1:
        return result
    # 1
    for num in arrays[0]:
        hashtable[num] = 1
    # 2
    for i in range(1,len(arrays)):
        for num in arrays[i]:
            if hashtable.get(num) is not None:
                hashtable[num] += 1
        
    result = [num for num in hashtable if hashtable[num] > 1]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
