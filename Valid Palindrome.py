class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while " " in s:
            s = s.replace(" ", "")
            s = s.replace(",", "")
            s = s.replace(":", "")
            s = s.replace(".", "")
            
            
        s = s.lower()
        if len(s) == 1:
            return True
        print(s)
        a = int(len(s))
        if s[0:a] == s[:-a-1:-1]:
            return True
        return False

s = Solution()

b = "a."
c = "A man, a plan, a canal: Panama."

s.isPalindrome(b)
print(s.isPalindrome(b))

s.isPalindrome(c)
print(s.isPalindrome(c))