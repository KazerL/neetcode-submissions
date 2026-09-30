from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # break
        if root is None:
            return []

        # initial var
        nodeList = []
        currSize = 0

        q = deque([root])

        while q:
            # level approach
            level = []

            for node in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            
            nodeList.append(level)

        return nodeList


