'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    i = 0
    # initialize the array of maximum numbers
    maxNums  = []
    # establish how far the window can move based on its size
    while i < len(nums) - k + 1:
        # the size of the window can be calculated by selecting all elements
        # from the current element to the current element plus k
        maxInWindow = max(nums[i:i+k])
        # the maximum value in the window is then added to the maxNums array and
        # the window moves on epsace to the right
        maxNums.append(maxInWindow)
        i += 1
        
    return maxNums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
