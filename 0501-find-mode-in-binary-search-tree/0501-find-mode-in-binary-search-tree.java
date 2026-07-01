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
    List<Integer> list=new ArrayList<>();
    int m=0,count=1,maxcount=0;
    TreeNode prev=null;
    public int[] findMode(TreeNode root) {
        inorder(root);
        int i=0;
        int arr[]=new int[list.size()];
        for(int num:list){
            arr[i++]=num;
        }
        return arr;
    }
    void inorder(TreeNode root){
        if(root==null) return ;
        inorder(root.left);
        if(prev!=null&& prev.val==root.val) count++;
        else count=1;
        if(count>maxcount) {
            maxcount=count;
            list.clear();
            list.add(root.val);
        }
        else if(count==maxcount) list.add(root.val);
        prev=root;      
        inorder(root.right);
    }
}