def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    hash_table = {}

    for i in range(len(weights)):

        target = limit - weights[i]
        if target in hash_table:
           return (i, hash_table[target])

        hash_table[weights[i]] = i

    return None


