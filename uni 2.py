def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first):
            if first == len(nums):
                result.append(nums[::])
            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1) 
                nums[first], nums[i] = nums[i], nums[first]
        result = []
        backtrack(0)
        return result
    
def swap(a, b):
    return b, a

    
#code agian backtracking
def func(nums):
    def backtrack(start):
        if start == len(nums):
           results.append(nums[::])
        for i in range(start, len(nums)):
           swap(nums[start], nums[i])
           backtrack(start + 1)
           swap(nums[i]. nums[start])
           
           
    results = []
    
    backtrack(0)
    return results
    


nums1 = [1, 2, 3]   
nums2 = [0,1]
print(func(nums1))
print(func(nums2))
