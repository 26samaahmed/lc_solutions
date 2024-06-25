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
    TreeNode* mergeTrees(TreeNode* root1, TreeNode* root2) {
        // if one of the trees is empty then return the other tree
        if (root1 == nullptr) {
            return root2;
        }
        if (root2 == nullptr) {
            return root1;
        }

        std::queue<TreeNode*> q1;
        std::queue<TreeNode*> q2;

        // push the root of each tree
        q1.push(root1);
        q2.push(root2);

        while (!q1.empty()) {
            TreeNode* node1 = q1.front();
            TreeNode* node2 = q2.front();

            // get the sum of both nodes and modify the value of node2 in place then pop the front of both queues
            node2->val +=  node1->val;
            q1.pop();
            q2.pop();

            // if there exists 2 values on both tree then enqueue both
            if (node1->left != nullptr and node2->left != nullptr) {
                q1.push(node1->left);
                q2.push(node2->left);
            }

            if (node1->right != nullptr and node2->right != nullptr) {
                q1.push(node1->right);
                q2.push(node2->right);
            }

            // if one of the nodes is null while the other isn't, then modify the value of node2's
            // left or right child in place
            if (node1->left != nullptr && node2->left == nullptr) {
                node2->left = node1->left;
            }

            if (node1->right != nullptr && node2->right == nullptr) {
                node2->right = node1->right;
            }

        }
        return root2;
    }
};