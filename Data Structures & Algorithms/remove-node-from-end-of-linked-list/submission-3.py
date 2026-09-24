class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initial var
        index = 0
        count = 0
        cur = head

        # count
        while cur:
            cur = cur.next
            count += 1
        
        # reset
        cur = head

        while cur:
            if n == 0:
                head = head.next
                return head
            if cur.next is None and index + 1 == n:
                head = head.next
                return head
            elif index + 1 == count - n and cur.next is not None:
                cur.next = cur.next.next
                return head
            cur = cur.next
            index += 1 
        


