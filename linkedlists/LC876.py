# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mid = head
        last = head
        while(last != None and last.next != None):
            mid = mid.next
            last = last.next.next
        return mid
    # Time Complexity: O(n)
    # Space Complexity: O(1)