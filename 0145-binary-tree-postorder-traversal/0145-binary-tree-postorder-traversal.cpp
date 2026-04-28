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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> lst;
        help(root,lst);
        return lst;
    }
    private:
    void help(TreeNode* root,vector<int>& lst){
        if(root){
            help(root->left,lst);
            help(root->right,lst);
            lst.push_back(root->val);
        }
    }
};