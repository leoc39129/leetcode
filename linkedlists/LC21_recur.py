# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def recurse(list1, list2):
            ret = None

            # Edge cases
            if list2 == None:
                return list1
            elif list1 == None:
                return list2

            # Get the head of the LL you wanna return
            if list1.val < list2.val:
                ret = list1
                list1 = list1.next
            else:
                ret = list2
                list2 = list2.next

            ret.next = recurse(list1, list2)
            return ret
        return recurse(l1, l2)
            
                    
                    
            
        
        
        
            
            