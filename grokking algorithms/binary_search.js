const binary_search = (item, array) => { 

    let  low = 0
    let high = length.array - 1
    let mid = 0
    let guess = 0
    while  low <= high:

        mid = (low + high) // 2 
        guess = list[mid]

        if guess === item { 
            return mid
        }

        if guess > mid {
            high = mid - 1
        }

        if guess  < mid { 
            low = mid + 1
        }

    return N


    

}
