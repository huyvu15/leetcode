class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        left = 1
        right = x
        mid = 0
        while (left <= right):
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
                sqrt = mid
        return sqrt

s = Solution()
a = s.mySqrt(8)
print(a)