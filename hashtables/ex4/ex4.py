def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    for i in a:
        if abs(i) in cache:
            result.append(abs(i))
        cache[abs(i)] = i

    return result

    



print(has_negatives([ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]))

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
