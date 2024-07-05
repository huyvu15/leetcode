class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            
            dividend -= temp_divisor
            quotient += multiple
        
        if negative:
            quotient = -quotient
        
        if quotient > 2**31 - 1:
            return 2**31 - 1
        elif quotient < -2**31:
            return -2**31
        
        return quotient



    
    
a = Solution()

print(a.divide(10, 3))
