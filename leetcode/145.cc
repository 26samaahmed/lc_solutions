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
    std::vector<int> postOrderList;
    void postOrder(TreeNode* root) {
        if (root == nullptr) return;
        postOrder(root->left);
        postOrder(root->right);
        postOrderList.push_back(root->val);

    }
    vector<int> postorderTraversal(TreeNode* root) {
        // post order means left then right then root
        postOrder(root);
        return postOrderList;
    }
};