class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = abs(n)
        if n == 0:
            return False
        if n == 1:
            return True
        while n >= 2:
            a = n%2            
            n = n/2
            if a != 0:
                return False
        else:
            return True
a = Solution()
a.isPowerOfTwo(16)
print(a.isPowerOfTwo(16))