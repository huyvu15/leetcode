class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = 0
        t_index = 0
        
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        
        return s_index == len(s)

a = Solution()
s = "axc" 
t = "ahbgdc"
a.isSubsequence(s,t)
print(a.isSubsequence(s,t))