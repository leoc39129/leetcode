# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Base Case:
        if not head or not head.next:
            return head

        OFF_LIMITS = 101
        # Here, the problem statement gives us that -100 <= Node.val <= 100
        # In practice, this could be a specified value that can never be used
        # in the linked list, or never will be used

        dummy = ListNode(OFF_LIMITS, head)
        greater = dummy
        less = dummy


        # The basic idea is run through the entire linked list, chaining
        # together the nodes with values less than x, and chaining together
        # all other nodes. This preserves order, as the problem statement requires

        # Using an OFF_LIMITS value to make sure that the greater or less node has
        # been assigned to a non-dummy node, you then go on to chain together the 
        # nodes properly, as aforementioned. The less_hold and greater_hold variables
        # store the beginnings of the chain of nodes with values less than x, and all
        # other nodes, respectively.

        run = head
        while run:
            if run.val < x:
                temp = run
                run = run.next
                if less.val != OFF_LIMITS:
                    less.next = temp
                    less = less.next
                else:
                    less = temp
                    less_hold = temp
            else:
                temp = run
                run = run.next
                if greater.val != OFF_LIMITS:
                    greater.next = temp
                    greater = greater.next
                else:
                    greater = temp
                    greater_hold = temp

        # At the end of this algoirthm, there will still
        # be a link between a node with a value greater than x and a node with a value
        # less than x -- for this reason, we hold the temp variable at the node previous 
        # to run. If that temp variable is a node where node.val < x, we know that a node
        # with a value greater than or equal to x must be pointing to a node with a value 
        # less than or equal to x, and vice versa. Break whichever link applies, which leads
        # to the final checks. 

        if temp.val < x:
            # Last node was less than target, break the connection between greater and less
            greater.next = None
        else:
            less.next = None


        # Not all cases will result in having a chain of nodes
        # with values greater than or equal to x, nor will all cases result in having a
        # chain of nodes less than or equal to x. Check whether or not both chains
        # exist, and connect the less chain to the greater chain (or don't) accordingly,
        # returning the correct starting point accordingly.

        if greater.val != OFF_LIMITS:
            less.next = greater_hold

        if less.val != OFF_LIMITS:
            return less_hold
        else:
            return greater_hold


'''
A great journey of a problem! Started off (mistakenly) using stacks to implement the approach below,
which made me realize I could just use LinkedLists instead. LeetCode says the below solution is...

RT: O(n)
Space O(1) (???)

Since I create another linked list of size n, I'm pretty sure this solution uses O(n) space.

Nevertheless, I pondered whether there was a way to write this algorithm with O(n) RT and O(1) space [actual O(1)],
and landed on the fact that I could rearrange the nodes and use no extra space (besides variables) to complete the task.
I explained it very thoroughly above, so read the comments if you don't understand the solution above. 

GPT also simplified the above solution a lot, using dummy nodes for the greater and less chains - not sure how I didn't
think of that, but now I know. GPT's solution is at the bottom.

class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Base Case:
        if not head or not head.next:
            return head

        dummy_less = ListNode(0)
        dummy_greater = ListNode(0)
        greater = dummy_greater
        less = dummy_less

        run = head
        while run:
            if run.val < x:
                less.next = ListNode(run.val)
                less = less.next
            else:
                greater.next = ListNode(run.val)
                greater = greater.next

            run = run.next

        less.next = dummy_greater.next

        return dummy_less.next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        # Dummy nodes to start less and greater partitions
        dummy_less = ListNode(0)
        dummy_greater = ListNode(0)
        
        less = dummy_less
        greater = dummy_greater
        current = head

        # Traverse the list, rearranging nodes
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        # Finalize the partitions by connecting less and greater lists
        greater.next = None  # Ensure no cycles by ending the greater list
        less.next = dummy_greater.next  # Connect end of less list to start of greater list

        return dummy_less.next


'''
        