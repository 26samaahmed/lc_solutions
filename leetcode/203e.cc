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
    ListNode* removeElements(ListNode* head, int val) {
        // create a copy of the head so i can use it to traverse through the list
        ListNode* temp = head;
        while (temp != nullptr) {
            if (head != nullptr && head->val == val) {
                head = head->next;
            } else if (temp->next != nullptr && temp->next->val == val) {
                 temp->next = temp->next->next;
            } else {
                temp = temp->next;
            }

        }
        return head;
    }
};
