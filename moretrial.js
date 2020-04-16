function fibonacci(n) {
    // create an empty array that will hold all values of the fib sequence 
    let arr = [];
    // base case condition that checks if the given number is equal to 1
    if (n == 1) {
        // return 0 in the array
        return [0]
    }
​
    // initialize first and second indices of the array, because it is required for fib
    arr[0] = 0;
    arr[1] = 1;
    // runa loop for as long as i < n
    for (let i = 2; i < n; i++) {
        //fib formula is ==>
        // f(n) = f(n-1) + f(n-2)
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    //return array
    return arr;
}

fibonacci(20)