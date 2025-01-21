
 // Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

using namespace std;
#include <algorithm>

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Base Cases: Empty LinkedLists Given
        if(!list1) {
            return list2;
        }
        if(!list2) {
            return list1;
        }
        
        // We will always return list1, set list1 to be the linked list with the smaller
        // starting value
        if(list1->val > list2->val) {
            // std::swap(list1, list2);
            ListNode* temp = list2;
            list2 = list1;
            list1 = temp;
        }

        // ret: head of the merged linked lists
        // temp: used as a placeholder when splicing a node from list2 into list1
        ListNode* ret = list1;
        ListNode* temp;

        /*
        As we iterate through list2, check to see if a node from list2 should be spliced
        in between two nodes from list1. This is accomplished in the first statement in the 
        if/else tree.

        If the value from list2 is larger than the value from list1, go to the next node in list1,
        if it exists. This is accomplished in the second statement in the if/else tree.

        If there are no more nodes in list1, this means that all nodes from list2 that should be 
        spliced into list1 have been inserted into the linked list. Therefore, the rest of list2
        should be "appended" to the end of list1, as if there are any nodes left in list2, the
        values of these nodes are guaranteed to be larger than the value of the last node in list1.
        If there are no more nodes in list2, the end of list1 will point to a null ptr. This is 
        accomplished in the last statement in the if/else tree.
        */
        while(list2) {
            if(list1->next && list2->val < list1->next->val) {
                temp = list1->next;
                list1->next = list2;
                list1 = list1->next;
                list2 = list2->next;
                list1->next = temp;
            } else if(list1->next) {
                list1 = list1->next;
            } else {
                list1->next = list2;
                break;
            }
        }

        return ret;
    }
};

// RT: O(n)
// Space: O(1)


// Here's the recursive code found in LeetCode's Editorial

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) {
            return l2;
        } else if (l2 == nullptr) {
            return l1;
        } else if (l1->val < l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        } else {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};

// RT: O(n)
// Space: O(n)
