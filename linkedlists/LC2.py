# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1.val == 0 and not l1.next:
            return l2
        if l2.val == 0 and not l2.next:
            return l1
        chain = ListNode(0)
        head = ListNode(0, chain)
        carry = 0
        while l2 and l1:
            temp = l2.val + l1.val + carry
            if temp < 10:
                chain.val = temp
                carry = 0
            else:
                chain.val = temp - 10
                carry = 1
            l2 = l2.next
            l1 = l1.next
            chain.next = ListNode(0)
            prev = chain
            chain = chain.next
        if not l2 and not l1:
            if carry == 0:
                prev.next = None
            else:
                chain.val = 1
        elif l2:
            while l2:
                temp = l2.val + carry
                if temp < 10:
                    chain.val = temp
                    carry = 0
                else:
                    chain.val = temp - 10
                    carry = 1
                chain.next = ListNode(0)
                prev = chain
                chain = chain.next
                l2 = l2.next
        else:
            while l1:
                temp = l1.val + carry
                if temp < 10:
                    chain.val = temp
                    carry = 0
                else:
                    chain.val = temp - 10
                    carry = 1
                chain.next = ListNode(0)
                prev = chain
                chain = chain.next
                l1 = l1.next
        if carry == 0:
            prev.next = None
        else:
            chain.val = 1
        return head.next
    
'''
RT: O(n)
Space: O(n)

Very long, somewhat unorganized, but it gets the job done. Using the same ideas
as the discussion board solutions. I missed how to use one while loop though...

"while l1 or l2 or carry"

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        dummy = ListNode()
        res = dummy

        total = carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            carry = total // 10
            dummy.next = ListNode(num)
            dummy = dummy.next
        
        return res.next
'''