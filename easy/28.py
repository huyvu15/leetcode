class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = len(needle)
        if a == 1 and len(haystack) == 1 and needle == haystack:
            return 0
        for i in range(len(haystack)):
            if haystack[i:i+a] == needle:
                return i


        return -1