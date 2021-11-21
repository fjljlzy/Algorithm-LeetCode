"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
      
        # dfs 1
        # if not root:
        #     return 0
        # ans = 1
        # for node in root.children:
        #     ans = max(self.maxDepth(node) + 1, ans)
        # return ans
        
        # dfs 2
        # if not root:
        #     return 0
        # ans = 0
        # for node in root.children:
        #     ans = max(ans, self.maxDepth(node))
        # return ans + 1

        # BFS
        if not root:
            return 0

        q = collections.deque()
        q.append(root)
        res = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for i in node.children:
                    q.append(i)
            res += 1
        return res
