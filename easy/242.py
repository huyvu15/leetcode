s = "ac" 

t = "ab"


# a = []
# b = []
# for i in range(len(s)):
#     a.append(ord(s[i]))
#     b.append(ord(t[i]))
# print(a, b)
# print(sum(a), sum(b))
# print(a.sort()== b.sort())

      
def i(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = []
        b = []
        for i in range(len(s)):
            a.append(ord(s[i]))
        for i in range(len(t)):
            b.append(ord(t[i]))
        if sum(a) == sum(b):
            return True
        return False
print(i(s, t))