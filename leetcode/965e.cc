/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isUnivalTree(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();

            if (node->left != nullptr && node->right != nullptr) {
                if (node->left->val != node->val || node->right->val != node->val) {
                    return false;
                } else {
                    q.push(node->left);
                    q.push(node->right);
                }
            } else if (node->right != nullptr) {
                if (node->right->val == node->val) {
                    q.push(node->right);
                } else {
                    return false;
                }
            } else if (node->left != nullptr) {
                if (node->left->val == node->val) {
                    q.push(node->left);
                } else {
                    return false;
                }
            }
        }
     return true;
    }
};

// with using a queue, edge cases i can think of are what if we reach a nullptr
// start by making a queue that contains the root and then loop until the q has elements
// if the left or right are not nullptr then check the values