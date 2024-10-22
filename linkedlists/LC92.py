# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # Base Case:
        if not head.next:
            return head

        dummy = ListNode(0, head)

        stack = []
        right_node = dummy

        while right > 0:
            right_node = right_node.next
            stack.append(right_node.val)
            right -= 1

        left_node = dummy
        while left > 0:
            left_node = left_node.next
            left -= 1

        #print(stack)
        while left_node != right_node:
            left_node.val = stack.pop()
            left_node = left_node.next
        
        left_node.val = stack.pop()

        return dummy.next
    

'''
Solved with O(n) RT, O(n) memory, but missed the O(n), O(1) solution below:

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        # Base Case:
        if not head.next or left == right:
            return head

        dummy = ListNode(0, head)

        prev = dummy
        ctr = left
        while ctr > 1:
            prev = prev.next
            ctr -= 1
        
        cur = prev.next

        for i in range(right-left):
            forward = cur.next
            cur.next = forward.next
            forward.next = prev.next
            prev.next = forward

        return dummy.next

'''


        