class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            if i == 0:
                if s[i] == 'I':
                    sum +=1
                elif s[i] == 'V':
                    sum +=5
                elif s[i] == 'X':
                    sum +=10
                elif s[i] == 'L':
                    sum +=50
                elif s[i] == 'C':
                    sum +=100
                elif s[i] == 'D':
                    sum +=500
                elif s[i] == 'M':
                    sum +=1000
            else: 
                if s[i] == 'I':
                    sum +=1
                elif s[i] == 'V':
                    if s[i-1] =="I":
                        sum-=2
                    sum +=5
                elif s[i] == 'X':
                    if s[i-1] == 'I':
                        sum -=2
                    elif s[i-1] == 'V':
                        sum -=10
                    sum +=10
                elif s[i] == 'L':
                    if s[i-1] == 'I':
                        sum -=2
                    elif s[i-1] == 'V':
                        sum -=10
                    elif s[i-1] == 'X':
                        sum -=20
                    sum +=50
                elif s[i] == 'C':
                    if s[i-1] == 'I':
                        sum -=2
                    elif s[i-1] == 'V':
                        sum -=10
                    elif s[i-1] == 'X':
                        sum -=20
                    elif s[i-1] == 'L':
                        sum -=100
                    sum +=100
                elif s[i] == 'D':
                    if s[i-1] == 'I':
                        sum -=2
                    elif s[i-1] == 'V':
                        sum -=10
                    elif s[i-1] == 'X':
                        sum -=20
                    elif s[i-1] == 'L':
                        sum -=100
                    elif s[i-1] == 'C':
                        sum -=200
                    sum +=500
                elif s[i] == 'M':
                    if s[i-1] == 'I':
                        sum -=2
                    elif s[i-1] == 'V':
                        sum -=10
                    elif s[i-1] == 'X':
                        sum -=20
                    elif s[i-1] == 'L':
                        sum -=100
                    elif s[i-1] == 'C':
                        sum -=200
                    elif s[i-1] == 'D':
                        sum -=1000
                    sum +=1000
            print(sum)
        return sum
    

s = Solution()
a = input("Nhập sâu s: ")
print(s.romanToInt(a))