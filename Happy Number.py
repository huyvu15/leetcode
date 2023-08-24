class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def tach(n):
            return sum(int(digit) ** 2 for digit in str(n))
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = tach(n)
        return n == 1
            
a = Solution()
a.isHappy(19)
print(a.isHappy(199))