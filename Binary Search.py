# Q) Given is a data and a target and asked to determine whether the target is present in the data

data = [2, 3, 5, 7, 9, 12, 14, 17, 19, 22, 24, 27, 31, 33, 37]
target = 25

# Two types of determining the presence of target : LINEAR SEARCH and BINARY SEARCH

# LINEAR SEARCH
# Basically runs through the whole data value by value checking for the target
# Good for small data-sets but very time-consuming in greater data-sets with millions of values

def linear_search(data, target):
    for i in range(len(data)) :
        if data[i] == target:
            return True
    return False


# BINARY SEARCH ---- ITERATIVE
# Sets a mid-point and cuts the data accordingly by looping through the data.  

def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:     #Cutting the data after-mid since mid is greater than target
            high = mid - 1
        else :
            low = mid + 1            #Cutting the data before-mid since mid is lower than target

    return False


# BINARY SEARCH ------- RECURSIVE
# Same as iterative, except we use recursion instead of looping.

def binary_search_recursive(data, target, low, high):
    if low > high :
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else :
            return binary_search_recursive(data, target, mid+1, high)
        
        return False

print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))