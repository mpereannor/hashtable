#O(logN)
def binary_search(item, list):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        #mid is rounded down by python automatically
        #if ( low + high ) isn't an even number
        mid = (low + high) // 2 
        guess = list[mid]

        if guess == item:
            return mid
        #if guess is high, we update high accordingly
        if guess > item:
            high = mid - 1

        #if guess is low, we update low accordingly
        if guess < item:
            low = mid + 1
    
    return None
    
dunder = [ 1, 2, 3, 4, 5]

binary_search(4,dunder)
print('name')

        
            