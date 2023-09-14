def counting_sort(arr):
    # Find the maximum value in the input array
    max_val = max(arr)
    
    # Initialize a list to store the count of each element
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

# Example usage
input_arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(input_arr)
print("Original Array:", input_arr)
print("Sorted Array:", sorted_arr)
