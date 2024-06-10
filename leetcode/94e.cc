/** Recursive Solution
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
    std::vector<int> inOrderVector;
    void inorder(TreeNode* root) {
        // Have base case
        if (root == nullptr){
            return;
        }
        inorderTraversal(root->left);
        inOrderVector.push_back(root->val);
        inorderTraversal(root->right);
    }

    vector<int> inorderTraversal(TreeNode* root) {
        // In order means go left then root then right
        inorder(root);
        return inOrderVector;
    }
};