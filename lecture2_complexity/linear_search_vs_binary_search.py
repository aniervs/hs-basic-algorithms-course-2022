from timeit import default_timer as timer

arr = []

def linear_search(x: int):
    '''
    Returns the position where x is, and returns None in case it doesn't exist in the array
    Time Complexity: O(n)
    '''
    for i in range(len(arr)):
        if arr[i] == x:
            return i 
    return None 

def binary_search(x):
    '''
    Returns the position where x is, and returns None in case it doesn't exist in the array
    Time Complexity: O(log n)
    '''
    l = 0
    r = len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid 
    if arr[l] == x:
        return l
    return None

for n in [10, 100, 1000, 10000, 100000, 10000000]:
    arr = [i for i in range(n)] # Creating a sorted array
    value = max(arr) + 1 # Value to search
    
    start = timer()
    linear_search(value)
    end_time = timer()
    print(f"Linear Search with n = {n}: {round(end_time - start, 6)}")

    start = timer()
    binary_search(value)
    end_time = timer()
    print(f"Binary Search with n = {n}: {round(end_time - start, 6)}")

    print()
    

