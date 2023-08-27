class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        
        short_str = min(strs, key = len)
        
        for i, char in enumerate(short_str):
            for other_str in strs:
                if other_str[i] != char:
                    return short_str[:i]
                
        return short_str
        
        
        
a  = Solution()
# Example usage
strs1 = ["flower", "flow", "flight"]
print(a.longest_common_prefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(a.longest_common_prefix(strs2))  # Output: ""