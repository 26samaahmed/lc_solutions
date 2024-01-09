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
    ListNode* reverseList(ListNode* head) {
        ListNode * current = head;
        ListNode * previous = nullptr;
        while (current != nullptr) {
            // store what the current node points at so i don't lose the link
            ListNode * next_ptr = current->next;
            // make the current node point at the node before it
            current->next = previous;
            // make the current node become the previous node so that in the next iteration the following node would point back at it
            previous = current;
            // move on to the next node
            current = next_ptr;
        }
        head = previous;
        return head;
    }
};
