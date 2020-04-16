def fibonacci(n):
    arr = []
    if n == 1:
        return [0]

    arr[0] = 0
    arr[1] = 1

    i = 2
    for i in n:
        arr[i] = arr[i - 1] + arr[i -2]
    return arr

fibonacci(10)