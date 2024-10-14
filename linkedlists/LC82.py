# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Base Case
        if not head:
            return None

        # Guaranteed to have one node
        if not head.next:
            return head

        # Guaranteed to have two nodes
        while head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            head = head.next

            if not head:
                return None

            if not head.next:
                return head

        # Starting with lead and trail having two distinct values
        lead = head.next
        trail = head

        while lead.next:
            if lead.val == lead.next.val:
                while lead.next and lead.val == lead.next.val:
                    lead = lead.next
                trail.next = lead.next
                lead = lead.next
            else:
                trail = trail.next
                lead = lead.next

            if not lead:
                return head

        return head
        
'''
Not the most elegant solution but it works. RT: O(n), O(1) space

An iterative solution

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        output = ListNode(0, head)
        pre = output
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        
        return output.next

A recursive solution

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next = head.next

        if next.val == head.val:
            while next and next.val == head.val:
                next = next.next
            return self.deleteDuplicates(next)
        else:
            head.next = self.deleteDuplicates(next)
            return head

An interesting Python solution that exploits the problem constraints

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        numbers_range = [0] * 201

        temp = head

        while temp:
            num = temp.val
            offset_val = num + 100
            numbers_range[offset_val] += 1
            temp = temp.next
        
        new_head = None
        temp = None

        for i in range(len(numbers_range)):
            freq = numbers_range[i]
            if freq > 1:
                continue
            elif freq == 1:
                if temp:
                    tail_node = ListNode(i-100)
                    temp.next = tail_node
                    temp = temp.next
                else:
                    new_head = ListNode(i-100)
                    temp = new_head
        
        return new_head
'''