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
    ListNode* deleteDuplicates(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        ListNode* temp = head;
        // if there's a duplicate in the end then skip and make it point to nullptr

        while (temp->next != nullptr) {
            // we would re link so have an if that check if the current node's value is
            // the same as the next node's value
            if (temp->next->next == nullptr && temp->val == (temp->next)->val) {
                temp->next = nullptr;
            } else if(temp->val == (temp->next)->val) {
                temp->next = temp->next->next;
            } else {
                temp = temp->next;
            }
        }
        return head;
    }
};