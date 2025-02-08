'''
4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3

Numbers:    1 2 3 4 5 6 
Occurence:  1 3 3 1 1 2
'''
def counting_sort(arr):
    max_value = max(arr) # Max length of the array
    new_arr = [0] * (max_value+1) # Initialize the new array
    #print("Max-length of the array: ", max_value)

    # Mapping each element of arr to increment the count at the index position of new_arr
    for num in arr:
        new_arr[num] += 1
    #print("Occurence: ", new_arr)

    # Calculate the prefix sum for the len(arr)/max_value+1
    for i in range(1, len(new_arr)):
        new_arr[i] += new_arr[i-1]
    #print("Prefix sum", new_arr)

    # New array
    '''
    We initialize i = len(new_arr) - 1 = 6 (last index of count array) and iterate backward using a while loop:

    When i = 6
    new_arr[6] = 11
    6 is placed at index 10 (new_arr[6] - 1).
    new_arr[6] is decremented to 10.
    6 is placed at index 9 (new_arr[6] - 1).
    new_arr[6] is decremented to 9.

    For eg: 
    final_arr[new_arr[6]-1]=6       final_arr[new_arr[5]-1]=5
    final_arr[11-1] = 6             final_arr[9-1]=5
    final_arr[10] = 6               final_arr[8]=5
    '''
    final_arr = [0] * len(arr)
    i = len(new_arr)-1
    while i >= 0: # Iterate in reverse order using while loop
        while new_arr[i] > 0: # If new_arr count is not zero, place the element in the final_arr
            final_arr[new_arr[i]-1] = i 
            new_arr[i] -= 1
        i -= 1
    return final_arr

if __name__ == '__main__':
    arr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
    print("Original array: ", arr)
    n = len(arr)
    sorted_array = counting_sort(arr)
    print("Sorted array: ", sorted_array)