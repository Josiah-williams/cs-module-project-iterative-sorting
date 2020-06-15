def linear_search(arr, target): # returns index of a key in array. Return -1 if target not present
    # Your code here

    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found

# the user enters a list of numbers 
# the user sets a target to search for 
# the array and target is passed thru linear_search
# if the return value is -1, the target is not found, otherwise the index of the found item will be displayed 

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    #figuring total size of array
    left = 0
    right= len(arr) -1

    while left <= right:
        #find the midpoint
        mid = (left + right) // 2

        #check to see if the midpoint element is our target
        if arr[mid] == target:
            return mid
        #check to see if the element should be on the right side or left side of our element
        if arr[mid] < target:
            #toss out the left side of the array
            #updates our left index
            left = mid +1
        #otherwise, arr[mid] > target
        else:
            # toss out the right side of the array because our element needs to be on the left side
            right = mid -1


    return -1  # not found
