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
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return helper(nums,0,nums.length-1);
    }
    TreeNode helper(int[] nums,int start,int end){
        if(start>end) return null;
        if(start==end) return new TreeNode(nums[start]);
        int idx=start;
        for(int i=start;i<=end;i++){
            if (nums[i]>nums[idx]) idx=i;
        }
        TreeNode root=new TreeNode(nums[idx]);
        root.left=helper(nums,start,idx-1);
        root.right=helper(nums,idx+1,end);
        return root;
    }
}