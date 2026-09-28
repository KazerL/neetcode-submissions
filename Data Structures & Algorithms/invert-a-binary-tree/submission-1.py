from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None

        q = deque([root])

        while q:
            # manages current node
            node = q.popleft()
            # child nodes
            left, right = node.left, node.right
            # swap logic
            leftCur = node.left
            node.left = node.right
            node.right = leftCur

            # adds remaining nodes
            if left:
                q.append(left)
            if right:
                q.append(right)

        return root

    
