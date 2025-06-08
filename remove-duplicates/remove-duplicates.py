# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        unique_list = list()
        for num in nums:
            if num not in unique_list:
                unique_list.append(num)
        for i in range(len(unique_list)):
            nums[i] = unique_list[i]
        print(nums)
        return len(unique_list)
    
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))