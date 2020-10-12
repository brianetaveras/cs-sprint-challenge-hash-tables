def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    length = len(arrays)
    cache = dict()
    
    for item in arrays[0]:
        cache[item] = 1


    for i in range(1, length):
        for item in arrays[i]:
            if item in cache:
                cache[item] += 1

    return [k for k,v in cache.items() if v is length]
    


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
