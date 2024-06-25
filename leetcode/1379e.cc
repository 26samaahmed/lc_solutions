/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        // think of this as bfs not dfs so use a queue to traverse this instead of going to the deepest child
        // start by creating a queue and pushing the root there

        std::queue<TreeNode*> q;
        q.push(cloned); // push the root first

        // start by checking if the current node is equal to target
        while (!q.empty()) {
            TreeNode* node = q.front();
            if (node->val == target->val) {
                return node;
            }
            // if the front is not the target we're looking for then pop it and then push both left and right nodes
            q.pop();
            if (node->left != nullptr) {
                q.push(node->left);
            }

            if (node->right != nullptr) {
                q.push(node->right);
            }

        }
        return nullptr;
    }
};