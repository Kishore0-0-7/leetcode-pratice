/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    TreeNode f=null;
    TreeNode s=null;
    TreeNode prev=null;
    public void recoverTree(TreeNode root) {
        inorder(root);
        int t=f.val;
        f.val=s.val;
        s.val=t;
    }
    void inorder(TreeNode root){
        if(root==null) return;
        inorder(root.left);
        if(prev!=null&&prev.val>root.val){
            if(f==null) f=prev;
            s=root;
        }
        prev=root;
        inorder(root.right);
    }
}