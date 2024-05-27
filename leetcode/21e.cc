/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Create a dummynode where we will start merging the 2 lists. Make sure that neither of the lists is empty. Then compare each list's current node's value
        // and adjust where temp points to based on that

        ListNode * list3 = new ListNode();
        ListNode * temp = list3;

        // as long as both lists are not empty then keep looping
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val < list2->val) {
                // make the current node point at the one from list1
                temp->next = list1;
                list1 = list1->next;
            } else {
                // make the current node point at the one from list2
                temp->next = list2;
                list2 = list2->next;
            } 
            temp = temp->next;
        }

        // If we went through one of the lists but we still have some nodes left in the other list, then just merge the leftover nodes to the merged list since they are already sorted
        if (list1 == nullptr) {
            temp->next = list2;
        } else if (list2 == nullptr) {
            temp->next = list1;
        }

        return list3->next;
    }
};