def fibonacci(n):
    #create an empty array that will hold all the values of the fib sequence
    #fibArr = [ 0, 1, 2, 3, 5, 8, 13, 21]
    fibArr = []

    #instantiate the first two indices of fibArr and assign
    #their default fib values
    fibArr[0] = 0
    fibArr[1] = 1

    #base case checks if the given number is less than or equal to 1
    if n == 0:
        return fibArr[0]
    elif n == 1:
        return fibArr[1]
    else:
        return fibArr[n-1] + fibArr[n-2]
    # #loop through fibArr as long as i < next
    # i = 0
    # while i < n:
    #     #return with fibonacci formula
    #     # f(n) = f(n - 1) + f(n -2)
    #     fibArr[i] = fibArr[i - 1] + fibArr[i - 2]

    # return fibArr

fibonacci(12)
