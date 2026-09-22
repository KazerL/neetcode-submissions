class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            # save node before breaking link
            nxt = cur.next
            # reverse the pointer
            cur.next = prev
            # move prev forward 
            prev = cur
            cur = nxt 
        
        return prev
        

