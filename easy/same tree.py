class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def dfs(p, q):
            if not p and not q:
                return True
            elif (p and not q) or (q and not p) or (p.val !=q.val):
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p,q) 
date = "2019-01-09"
print(int(date[8:10]))
print(int(date[5:7]))
print(int(date[0:4]))


for i in range(1, 2):
    print(i)