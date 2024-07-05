class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        ma = [[0] * n for _ in range(len(matrix))]  # Đây là tham chiếu tới cùng một đối tượng, hãy chú ý
        for i in range(n):
            for j in range(n):
                ma[i][j] = matrix[j][i]  # Đảo vị trí như bạn muốn
        for i in range(n):
            ma[i].reverse()
        return ma

a = Solution()

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

a.rotate(matrix)
print(a.rotate(matrix))
