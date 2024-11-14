# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # Base Case:
        if not head or not head.next:
            return False

        run = head
        SEEN_VALUE = -1000000
        while run:
            if run.val == SEEN_VALUE:
                return True
            run.val = SEEN_VALUE
            run = run.next

        return False


'''
RT: O(n)
Space: O(1)

This approach is slightly scummy, as you modify the linked list, but I already knew the two pointer
fast/slow approach. Easy and well done!

Below is the O(n), O(1) way to do it without modifying the list

class Solution:
    def hasCycle(self, head):
    
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
    
        return False
'''