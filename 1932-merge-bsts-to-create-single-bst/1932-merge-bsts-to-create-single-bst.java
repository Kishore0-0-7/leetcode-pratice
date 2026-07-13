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
    public TreeNode canMerge(List<TreeNode> trees) {
      Set<Integer> set=new HashSet<>();
      Map<Integer,TreeNode> map=new HashMap<>();
      for(TreeNode root:trees){
        map.put(root.val,root);
        if(root.left!=null) set.add(root.left.val);
        if(root.right!=null) set.add(root.right.val);
      } 
      TreeNode result=null;
      for(TreeNode root:trees){
        if(!set.contains(root.val)){
            result=root;
            break;
        }
      }
      if(result==null) return null;
      return Traverse(result,Integer.MIN_VALUE,Integer.MAX_VALUE,map)&&map.size()==1?result:null;
    }
    boolean Traverse(TreeNode result,int min,int max,Map<Integer,TreeNode>map){
        if(result==null) return true;
        if(result.val<=min||result.val>=max) return false;
        if(result.left==null&&result.right==null){
            if(map.containsKey(result.val)&&map.get(result.val)!=result){
                TreeNode next=map.get(result.val);
                result.left=next.left;
                result.right=next.right;
                map.remove(result.val);
            }
        }
        return Traverse(result.left,min,result.val,map)&&Traverse(result.right,result.val,max,map);
    }
}