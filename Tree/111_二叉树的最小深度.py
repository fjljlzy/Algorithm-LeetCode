class Solution:
  '''
  这道题求的是最小深度，一般题目求的都是最大深度。
  细节十分恶心。
  '''
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.right and root.left:
            return 1 + self.minDepth(root.left)
        elif not root.left and root.right:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
