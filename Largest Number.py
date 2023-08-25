class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = ''.join([str(char) for char in nums])
        nums = list(nums)
        nums.sort()
        nums.reverse()
        nums = ''.join([str(char) for char in nums])
        print(nums)
        

a = Solution()

nums = [3,30,34,5,9]

a.largestNumber(nums)