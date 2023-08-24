class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls = []
        
        for i in range(len(s)):
            for j in range(len(s)):
                ls.append(s[i:j:])
        
        print(ls)
        lb = []
        for i in ls:
            a = int(len(i)/2)
            if i[0:a] == i[:-a-1:-1] and len(i) >1:
                # print(i)
                lb.append(i)
        print(lb)
        print(max(lb))
        return max(lb)
        
        
        # ls = []
        # for i in range(len(s)):
        #     for j in range(len(s)):
        #         if s[i:j:] == s[-i:-j:-1]:
        #             ls.append(s[i:-j:])
        # print(max(ls))
        # return max(ls)        
        # d = s.strip()
        # a = d.split(" ")
        # len1 = len(a)
        # b = int(len1/2)

        # if a[0:b]==a[:-b-1:-1]:
        #     print("a")
        # else:
        #     print("NOT Word Palindrome")
            

class Solution1(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        longest = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub_str = s[i:j+1]
                if sub_str == sub_str[::-1] and len(sub_str) > len(longest):
                    longest = sub_str
                    
        return longest

a = Solution1()
s = "babad"
a.longestPalindrome(s)
print(a.longestPalindrome(s))