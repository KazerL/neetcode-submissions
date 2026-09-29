class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def path(node, target):
            # base cases
            if not node:
                return None
            
            if node.val == target.val:
                return [node.val]
            
            # searches the entire left subtree first
            alt = path(node.left, target) or path(node.right, target)
            
            # alt is either a path or none
            if alt:
                return alt + [node.val]
            else:
                return None
        
        def fetch(node, target):
            if not node:
                return None
            
            if node.val == target:
                return node

            return fetch(node.left, target) or fetch(node.right, target)

        path1 = path(root, p)
        path2 = path(root, q)

        compare = set()


        for node in path1:
            compare.add(node)

        for node in path2:
            if node in compare:
                return fetch(root, node)
            else:
                continue
        
        return None
            
        



        