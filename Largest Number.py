class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = ''.join([str(char) for char in nums])
        print(nums)
        nums = list(nums)
        print(nums)
        nums.sort()
        nums.reverse()
        nums = ''.join([str(char) for char in nums])
        print(nums) 
    def bigNums(self, nums):
        "a"
        new = []
        for i in range(len(nums)):
            digit = str(nums[i])
            save = nums[i] / (10**(len(digit)-1))
            print(nums[i], save)
    def test(self, nums):
        nums_str = [str(num) for num in nums]

        # Sort the numbers using the custom comparison function
        nums_str.sort(key=lambda x: (x, x[::-1]), reverse=True)

        # Handle the case where the input contains only zeros
        if nums_str[0] == '0':
            return '0'

        # Concatenate the sorted numbers to form the largest number
        largest_num = ''.join(nums_str)

        return largest_num
        

a = Solution()

nums = [3,30,34,5,9]

# a.largestNumber(nums)
# a.bigNums(nums)
print(a.test(nums))

