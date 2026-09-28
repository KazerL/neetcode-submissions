from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # break case
        if q is None and p is None:
            return True
        elif q is None or p is None:
            return False

        queue1 = deque([q])
        queue2 = deque([p])

        # comparisons
        list1 = []
        list2 = []

        while queue1:
            node = queue1.popleft()
            
            if node is None:
                list1.append(None)
                continue

            list1.append(node.val)
            left, right = node.left, node.right

            queue1.append(left)
            queue1.append(right)
        
        while queue2:
            node = queue2.popleft()

            if node is None:
                list2.append(None)
                continue

            list2.append(node.val)
            left, right = node.left, node.right

            queue2.append(left)
            queue2.append(right)
        
        if list1 == list2:
            return True
        else: 
            return False
