# ITERATIVE SOLUTION

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = None
        trav = None
        
        # Edge cases
        if list1 == None and list2 == None:
            return None
        elif list2 == None:
            return list1
        elif list1 == None:
            return list2
        
        # Get the head of the LL you wanna return
        if list1.val < list2.val:
            ret = list1
            trav = list1
            list1 = list1.next
        else:
            ret = list2
            trav = list2
            list2 = list2.next
        
        # Cycle through each list, easy!
        while list1 != None or list2 != None:
            if list1 == None:
                trav.next = list2
                break
            elif list2 == None:
                trav.next = list1
                break
            elif list1.val < list2.val:
                trav.next = list1
                list1 = list1.next
                trav = trav.next
                trav.next = None
            else:
                trav.next = list2
                list2 = list2.next
                trav = trav.next
                trav.next = None
        return ret
    
'''
Came back to this problem a while later, nailed it

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Base Case
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Dummy Node for returning
        ret = ListNode(0)
        
        if list2.val < list1.val:
            ret.next = list2
            trail = list2
            list2 = list2.next
        else:
            ret.next = list1
            trail = list1
            list1 = list1.next

        while list1 or list2:
            if list1 and list2:
                # Compare values, link up the smaller val
                if list2.val < list1.val:
                    trail.next = list2
                    list2 = list2.next
                    trail = trail.next
                else:
                    trail.next = list1
                    list1 = list1.next
                    trail = trail.next
            elif list1:
                trail.next = list1
                list1 = list1.next
                trail = trail.next
            else:
                # list2
                trail.next = list2
                list2 = list2.next
                trail = trail.next

        return ret.next
'''
            
                    
                    
            
        
        
        
            
            