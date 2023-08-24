class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n >1:
            a = n % 4
            n = n/4
            if a != 0: 
                return False
        else:
            return True

    
a = Solution()
print(a.isPowerOfFour(16))