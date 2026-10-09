from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque([root])
        string = []

        while q:
            node = q.popleft()
        
            if node is None:
                string.append("n")
                continue
            
            string.append(str(node.val))

            q.append(node.left)
            q.append(node.right)

        return ",".join(string)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        string = data.split(",")
        root = TreeNode(str(string[0]))

        # break condition
        if string[0] == "n":
            return None

        q = deque([root])
        i = 1

        while q:
            parent = q.popleft()

            if string[i] != "n":
                parent.left = TreeNode(int(string[i]))
                q.append(parent.left)
            
            i += 1

            if string[i] != "n":
                parent.right = TreeNode(int(string[i]))
                q.append(parent.right)

            i += 1
        
        return root

