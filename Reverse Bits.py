class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # n = str(n)
        n = n[::-1]
        print(int(n, 2))
    
s = Solution()
n = '00000010100101000001111010011100'
s.reverseBits(n)