# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
        # allsum = []
        # for i in range(len(nums)-1):
        #     sum = 0
        #     sum += nums[i] + nums[i+1]
        #     for j in range(len(nums)-1):
        #         if i != j and i != j+1:
        #             allsum.append(sum + nums[j])
        # allsum.sort()  
        # dicts = {}
        # for ele in allsum:
        #     if ele in dicts:
        #         dicts[ele] += 1
        #     else:
        #         dicts[ele] = 1

        # # print(dicts)
        
        # result_list = [key for key, value in dicts.items() if value > 1]

        # print(result_list)
        # # print(allsum)            
        # save = []
        # for i in range(len(nums)-1):
        #     sum = 0
        #     sum += nums[i] + nums[i+1]
        #     for j in range(len(nums)-1):
        #         a = []
        #         if i != j and i != j+1 :
        #             if sum + nums[j] in result_list:
        #                 a.append(nums[i])
        #                 a.append(nums[i+1])
        #                 a.append(nums[j])
                    
        #         if len(a) > 0:
        #             save.append(a)
        # return save
        #     save.append(a)
        # print(save)
        
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if i and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                a, b, c = nums[i], nums[j], nums[k]
                x = a + b + c
                if x == 0:
                    ans.append([a, b, c])
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    j += 1
                    k -= 1
                elif x < 0:    
                    j = j + 1
                else:
                    k -= 1
        print(ans)
                    
class Solution2(object):
    def THREESum(self, nums):
        nums.sort()   
        n = len(nums)
        ans = []
        
        for i in range(n - 2):
            if i and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                a, b , c = nums[i] , nums[j] , nums[k]
                x = a + b + c
                if x == 0:
                    ans.append([a, b, c])
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    j = j + 1
                    k = k - 1
                elif x < 0:
                    j = j + 1
                else: 
                    k = k - 1   
        print(ans)  
        
                           
a = Solution2()

nums = [-1,0,1,2,-1,-4]
print("nums = ",nums)
a.THREESum(nums)
# print(a.threeSum(nums))