class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        bi = int(a)+int(b)
        d = []
        while bi != 1:
            z = bi
            bi = bi//2
            c = z - bi*2
            d.append(str(c))
        d = d[::-1]  
        return ''.join(d)
        
        
s = Solution()

a = '11'
b = '1'

s.addBinary(a, b)

g = int(a, 2)
print(g)