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
        // Start by creating a 3rd list that will combine both
        // Then start by checking that if both head's of the list don't point to nullptr (not empty)
        // then check if list 1's current node's value is less than list 2's current node's value.
        // if it is then push to list 3. If list 2's current node's value is less than the node in list 1 then push it to list 3.
        // Note that if they're equal, then just push both nodes to list 3 since the order of the 2 nodes won't matter in this case

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

        // What if one of the lists is empty
        if (list1 == nullptr) {
            temp->next = list2;
        } else if (list2 == nullptr) {
            temp->next = list1;
        }

        return list3->next;
    }
};