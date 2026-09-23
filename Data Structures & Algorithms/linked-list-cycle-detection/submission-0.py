# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.visited = False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        
        while cur:
            if cur.next == None:
                return False
            if cur.next.visited == True:
                return True
            cur.visited = True
            cur = cur.next

        return False