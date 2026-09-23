# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        duplicate = set()

        cur = head

        while cur:
            if cur not in duplicate:
                duplicate.add(cur)
                cur = cur.next
            else:
                return True

        return False