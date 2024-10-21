# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Base Case:
        if not head:
            return None
        
        temp = head
        n = 1
        while temp.next:
            n += 1
            temp = temp.next

        k = k % n

        counter = 1
        new_tail = head
        while counter < n - k:
            new_tail = new_tail.next
            counter += 1
        
        temp.next = head
        head = new_tail.next
        new_tail.next = None

        return head


'''
Done in 10 mins, great job.

Discussion board has the same approach, RT O(n), Space O(1)
Missed two base cases: if there's just one node, and if k == 0 after the modulo

    # Base Case:
    if not head or not head.next:
        return None

    temp = head
        n = 1
        while temp.next:
            n += 1
            temp = temp.next
    k = k % n
    
    if k == 0:
        return head
'''