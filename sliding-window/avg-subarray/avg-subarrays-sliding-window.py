"""
Let’s understand this problem with a real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Here, we are asked to find the average of all contiguous subarrays of size ‘5’ in the given array. Let’s solve this:

For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5 => 2.2(1+3+2+6−1)/5=>2.2
The average of next 5 numbers (subarray from index 1-5) is: (3+2+6-1+4)/5 => 2.8(3+2+6−1+4)/5=>2.8
For the next 5 numbers (subarray from index 2-6), the average is: (2+6-1+4+1)/5 => 2.4(2+6−1+4+1)/5=>2.4
…
Here is the final output containing the averages of all contiguous subarrays of size 5:

Output: [2.2, 2.8, 2.4, 3.6, 2.8]

Time complexity = O(n)
n is length of array

"""
def avg_subarray(count, arr):
    avg = []
    startEle = 0
    curr_sum = 0.0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if i >= count-1:
            avg.append(curr_sum/count)
            curr_sum = (curr_sum - arr[startEle])
            startEle += 1
    return avg


arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
count = 5
avg = []
if count > len(arr):
    print("Length of array=" + str(len(arr)) + " smaller than count=" + str(count))
else:
    print(avg_subarray(count, arr))
