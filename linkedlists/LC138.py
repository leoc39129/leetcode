# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # Base Case:
        if not head:
            return None

        # Make the head of the deep copy
        copy_head = Node(head.val, None, None)
        run_copy = copy_head

        # Dictionary will translate a node from the original list
        # to a node from the copied list, so that each node's random
        # can be filled in later with O(1) lookup 
        copy_dict = {}
        copy_dict[head] = copy_head

        run = head.next

        # Create the copied list, with each node's next being filled in
        while run:
            run_copy.next = Node(run.val, None, None)
            run_copy = run_copy.next

            copy_dict[run] = run_copy

            run = run.next

        run = head
        run_copy = copy_head

        # Fill in each copied node's random, using the dictionary made
        # as the original list was iterated through the first time
        while run:
            if run.random:
                run_copy.random = copy_dict[run.random]

            run = run.next
            run_copy = run_copy.next

        return copy_head

'''
RT: O(n)
Space: O(n)

There is a O(n) RT, O(1) space solution involving interleaving new nodes into the original list and 
then disconnecting them, but I missed that solution. Next time!

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        copy_head = Node(head.val, None, None)
        run_copy = copy_head
        run = head.next

        while run:
            run_copy.next = Node(run.val, None, None)
            run_copy = run_copy.next

            # print(run.random)
            run = run.next

        run = head
        run_copy = copy_head
        while run:
            random = run.random
            if random:
                temp = head
                ctr = 0
                while temp != random:
                    temp = temp.next
                    ctr += 1

                temp_copy = copy_head
                for _ in range(ctr):
                    temp_copy = temp_copy.next
                run_copy.random = temp_copy

            run = run.next
            run_copy = run_copy.next

        return copy_head
'''   