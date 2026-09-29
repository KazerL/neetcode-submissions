from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            # recurisve base case
            if a is None and b is None:
                return True
            # fail case
            if a is None or b is None or a.val != b.val:
                return False
            
            # recursion itself
            return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)
        
        # break case
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False

        q = deque([root])

        while q:
            node = q.popleft()

            if node is None:
                continue

            left, right = node.left, node.right

            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True

            q.append(left)
            q.append(right)
        
        return False

    
        
    
        
        