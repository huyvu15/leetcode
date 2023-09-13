def partition(s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        temp = []
        for i in range(len(s)):
            temp.append(s[i])
        ans.append(temp)
        print(ans)
        
        
        
s = "aab"

partition(s)