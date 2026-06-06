/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool evaluateTree(struct TreeNode* root) {
    if (root->left == NULL && root->right ==NULL){
            if (root->val==0)
                return false;
            return true;
        }
        bool left=evaluateTree(root->left);
        bool right=evaluateTree(root->right);

        if (root->val==2) return left || right;
        return left && right;
}