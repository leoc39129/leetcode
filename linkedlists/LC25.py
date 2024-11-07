# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Base Case:
        if not head.next or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        lead = dummy
        trail = dummy

        while True:
            trail = lead
            for num in range(k-1):
                if lead.next:
                    lead = lead.next        
                else:
                    return dummy.next
            switches = k
            for _ in range(switches):
                self.switchNodes(lead, trail)

            if True:    # obviously this condition needs to be replaced
                break
                
        return dummy.next

    def switchNodes(self, lead, trail):
        # if the nodes are right next to eachother, different protocol?
        temp = lead.next.next
        lead.next.next = trail.next.next
        trail.next.next = temp

        temp = trail.next
        trail.next = lead.next
        lead.next = temp


'''
Decent attempt, this is a LC hard. Hard to get all these moving pieces to work together.

Discussion board solutions are garbage. Here's GPT:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Step 1: Count the number of nodes in the list
        node_count = 0
        current = head
        while current:
            node_count += 1
            current = current.next

        # Step 2: Initialize pointers
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while node_count >= k:
            # Step 3: Reverse k nodes
            prev = None
            current = group_prev.next
            next_node = None

            # Reverse k nodes
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            # Step 4: Connect the reversed group with the previous part
            tail = group_prev.next
            tail.next = current  # Connect the last node of the reversed part to the rest
            group_prev.next = prev  # Connect the previous part to the first node of the reversed part

            # Step 5: Move the group_prev pointer forward
            group_prev = tail
            node_count -= k

        return dummy.next

'''