import heapq

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        nodeList = []
        index = 0
        
        def smallest(node):
            if not node:
                return True

            
            nodeList.append(node.val)

            return smallest(node.left) and smallest(node.right)
        
        # has to be below
        smallest(root)

        nodeList.sort()

        for node in nodeList:
            if index == (k - 1):
                return node
            else:
                index += 1
                continue

        
        return -1


        