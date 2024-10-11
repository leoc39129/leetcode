# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # Base Case: If there's only one node, problem specs dictate that we MUST
        # return an empty list
        if not head.next:
            return None
        
        # Iterate through the list keeping track of two nodes, 
        # the current one and one with a n delay

        # Meaning, we want the delayed node to end up at the node before the node 
        # we want to remove (really, it's a n+1 delay), that way we can easily
        # excise it (SEE: if counter > n + 1)

        cur = head
        delay = head

        counter = 0
        while cur:
            cur = cur.next
            counter += 1
            if counter > n + 1:
                delay = delay.next

        # The counter variable will end up with the total number of nodes in the
        # linked list. If n == counter, we're removing the head of the list,
        # as we're asked to remove the nth node from the end of the list
        
        if counter == n:
            return head.next

        temp = delay
        temp = temp.next
        if temp.next:
            delay.next = temp.next
        else:
            delay.next = None

        return head
    
'''
Done in <30 mins! Good job

Here's an interesting alternative, with a fast node that jumps out to a n step head start,
and a slow node that takes the same number of steps as fast does to the end of the linked
list. Notice the "if not fast: return head.next" -- it takes the same role as our
"if counter == n: return head.next" statement above. Plus, no base case!

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
'''