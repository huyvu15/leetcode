class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        last_non_zero_index = 0 
        
        for i in range(len(nums)):
            if nums[i] != 0:
                swap(i, last_non_zero_index)
                last_non_zero_index += 1
        return nums
    
a = Solution()

print(a.moveZeroes([0, 1, 0, 3, 12]))