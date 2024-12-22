#Brute Force

arr = [1, -2, 3, 5, -1, 2]
n = len(arr)

# def max_subarray(arr, n):
#        max_sum 


#Sliding Window
k = 3

def max_subarray(arr, k):
    sub_array = sum(arr[:3])
    max_sum = sub_array
    global index
    index = 0
    for i in range(len(arr) - k):
        sub_array += arr[k+1] - arr[i]
        index = i + 1
        if(sub_array > max_sum):
            max_sum = sub_array
        
    return max_sum

print(f"Maximum sum is {max_subarray(arr, k)}")
for i in range(index, n):
    print(f"{arr[i]}")