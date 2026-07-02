/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val=val;}
 *     TreeNode(int val,TreeNode left,TreeNode right) {
 *         this.val=val;
 *         this.left=left;
 *         this.right=right;
 *     }
 * }
 */
class Solution {
    List<List<String>> res;

    public List<List<String>> printTree(TreeNode root){
        res=new ArrayList<>();
        int rows=getHeight(root);
        int cols=(int) Math.pow(2,rows)-1;
        for(int i=0;i<rows;i++){
            res.add(new ArrayList<>());
            for(int j=0;j<cols;j++){
                res.get(i).add("");
            }
        }
        fill(root,0,0,cols-1);
        return res;
    }

    private void fill(TreeNode root,int r,int cStart,int cEnd){
        if(root==null) return;
        int mid=(cStart+cEnd)/2;
        res.get(r).set(mid,String.valueOf(root.val));
        fill(root.left,r+1,cStart,mid-1);
        fill(root.right,r+1,mid+1,cEnd);
    }

    private int getHeight(TreeNode root){
        if(root==null) return 0;
        return 1+Math.max(getHeight(root.left),getHeight(root.right));
    }
    

}