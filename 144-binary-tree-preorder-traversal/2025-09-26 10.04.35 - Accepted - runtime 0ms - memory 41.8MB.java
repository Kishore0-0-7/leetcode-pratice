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
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> lst=new ArrayList<>();
        help(root,lst);
        return lst;
    }
    private void help(TreeNode root,List<Integer> lst){
        if(root!=null){
            lst.add(root.val);
            help(root.left,lst);
            help(root.right,lst);
        }
    }
}