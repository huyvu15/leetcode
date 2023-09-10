class Solution:
    def fourSum(self, nums, target):
        " "
        nums.sort()
        n = len(nums)   
        ans = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i] - 1:
                continue
            for j in range(i+1, n - 2):
                if j > 0 and nums[j] == nums[j] - 1:
                    continue
                m = j + 1
                k = n - 1
                while m < k:
                    a, b, c, d = nums[i], nums[j], nums[m], nums[k]
                    x = a + b + c + d
                    if x == target:
                        ans.append([a, b, c, d])
                        while m < k and nums[m] == nums[m-1]: m += 1
                        while m < k and nums[k] == nums[k-1]: k += 1
                        m = m + 1
                        k = k - 1
                    elif x < target:
                        m +=1
                    else:
                        k = k-1
        return ans
                         
                
a = Solution()
nums = [1,0,-1,0,-2,2]
target = 0


print(a.fourSum(nums, target))
