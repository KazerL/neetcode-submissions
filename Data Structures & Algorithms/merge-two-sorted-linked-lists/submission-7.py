class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initial var
        copy = []
        index = 0

        # merging into list 2
        cur1 = list1
        cur2 = list2

        if list1 is None and list2 is None:
            return list1
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        dummy2 = ListNode(float('-inf'), list2)   # new
        cur1 = list1
        cur2 = dummy2                             # was: cur2 = list2


        while cur1:
            if cur2.next is None:
                cur2.next = cur1
                break
            if cur2.val <= cur1.val and cur1.val < cur2.next.val:
                nxt1 = cur1.next
                cur1.next = cur2.next
                cur2.next = cur1
                cur1 = nxt1
            else:
                cur2 = cur2.next
        
        return dummy2.next

