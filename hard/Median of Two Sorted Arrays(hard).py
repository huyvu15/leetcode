nums1 = [1,2]
nums2 = [3,4]


def d(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = nums1 + nums2
        sum1 = 0
        
        for i in range(int(len(num)/2)):
            sum1 = sum1 + num[i] + num[-i]

        return sum1
    
print(d(nums1, nums2))


