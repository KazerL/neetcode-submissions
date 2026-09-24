class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # pointers
        cur = head
        fast = cur.next
        slow = cur

        # seperating the two linked lists
        while fast and fast.next:
            slow = slow.next
            if fast.next.next is None:
                break
            else:
                fast = fast.next.next

        fast = slow.next
        slow.next = None

        # reverse the second list
        prev = None
        while fast:
            nxt = fast.next
            fast.next = prev
            prev = fast
            fast = nxt

        second = prev

        # merging the two linked lists
        while second:
            nxt1 = cur.next
            nxt2 = second.next

            cur.next = second
            second.next = nxt1
            cur = nxt1
            second = nxt2
        
        return second
        
