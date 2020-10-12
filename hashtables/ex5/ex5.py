def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    cache = dict()
    for file in files:
        last = file.split("/")[-1]
        if last not in cache:
            cache[last] = []
        cache[last].append(file)

    for query in queries:
        if query in cache:
            for file in cache[query]:
                result.append(file)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))