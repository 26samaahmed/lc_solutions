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
    int maxDepth(TreeNode* root) {
        // base case so recurse until we reach the leaf
        if (root == nullptr) {
            return 0;
        }
        // we ge the maximum by comparing the length of each subtree and add 1 to it
        return std::max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};