# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# Example 1:
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

class Solution(object):
    def shuffle(self, nums, n):
        if not nums:
            return
        x_arr = nums[0:n]
        y_arr = nums[n:]
        max_arr = max(x_arr, y_arr, key=len)
        shuffle_arr = list()
        for i in range(len(max_arr)):
            if i < len(x_arr):
                shuffle_arr.append(x_arr[i])
            if i < len(y_arr):
                shuffle_arr.append(y_arr[i])
        return shuffle_arr
        
sol = Solution()
sol.shuffle([1,2,3,4,4,3,2,1], 4)