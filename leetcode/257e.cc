class Solution {
public:
    vector<string> v;
    void traverse(TreeNode* root, string temp) {
        if (root == nullptr) {
            temp = "";
            return;
        }

        if (root->left == nullptr && root->right == nullptr) {
            temp.append(to_string(root->val));
            v.push_back(temp);
        } 
        temp.append(to_string(root->val));
        temp.append("->");
            

        traverse(root->left, temp);
        traverse(root->right, temp);

    }
    vector<string> binaryTreePaths(TreeNode* root) {
        traverse(root, "");
        return v;
    }
};