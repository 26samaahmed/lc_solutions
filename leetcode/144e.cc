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
    std::vector<int> preorderList;
    void preOrder(TreeNode* root) {
        if (root == nullptr) return;
        preorderList.push_back(root->val);
        preOrder(root->left);
        preOrder(root->right);

    }
    vector<int> preorderTraversal(TreeNode* root) {
        // preorder means root then left then right
        preOrder(root);
        return preorderList;
    }
};