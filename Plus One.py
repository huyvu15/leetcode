class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        size = len(digits)
        total = 0
        for i in range(size):
            total += digits[i] * (10 ** (size - i - 1))
        total += 1
        results = []
        while total > 0:
            remainder = total % 10
            results.append(remainder)
            total = total // 10
        results.reverse()  # Đảo ngược danh sách
        return results

a = Solution()
print(a.plusOne([9, 9]))
