'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    zeroArr = []
    i = 0
    
    while i < len(arr):
        # if the value of the current index is 0, add it to zeroArr and remove
        # it from the current array
        
        # the pointer isn't moved in case the ollowing index
        # which becomes the current index is also a zero
        if arr[i] == 0:
            zeroArr.append(arr[i])
            arr.remove(arr[i])
        # if it isn't zero, the point
        else:
            i += 1
            
    # once loop above is finished, every element from the zeroArr is appended
    # to the current array
    for i in zeroArr:
        arr.append(i)
        
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")