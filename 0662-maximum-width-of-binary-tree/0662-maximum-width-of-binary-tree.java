/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val=val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val=val;
 *         this.left=left;
 *         this.right=right;
 *     }
 * }
 */
class Pair {
    TreeNode node;
    int index;
    Pair(TreeNode n, int i) {
        node=n;
        index=i;
    }
}
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        int result=-1;

        Queue<Pair> queue=new LinkedList<>();
        queue.add(new Pair(root ,0));

        while(!queue.isEmpty()) {
            int levelLength=queue.size();
            int idx=0;
            int startAt=queue.peek().index;

            for(int i=0; i < levelLength; i++) {
                Pair pair=queue.poll();
                TreeNode curr=pair.node;
                idx=pair.index;

                if(curr.left != null) queue.add(new Pair(curr.left, 2 * idx + 1));
                if(curr.right != null) queue.add(new Pair(curr.right, 2 * idx + 2));
            }
            result=Math.max(result, idx-startAt+1);
        }
        return result;
    }
}