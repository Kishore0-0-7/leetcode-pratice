/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val=x; }
 * }
 */
class Solution {

    Map<TreeNode,TreeNode> parentMap=new HashMap<>();

    private void buildParent(TreeNode node,TreeNode parent) {
        if (node == null) return;

        parentMap.put(node,parent);
        buildParent(node.left,node);
        buildParent(node.right,node);
    }

    public List<Integer> distanceK(TreeNode root,TreeNode target,int k) {

        buildParent(root,null);

        Queue<TreeNode> queue=new LinkedList<>();
        Set<TreeNode> visited=new HashSet<>();

        queue.offer(target);
        visited.add(target);

        int distance=0;

        while (!queue.isEmpty()) {

            int size=queue.size();

            if (distance==k) {
                List<Integer> ans=new ArrayList<>();
                while (!queue.isEmpty()) {
                    ans.add(queue.poll().val);
                }
                return ans;
            }
            for (int i=0; i<size; i++) {
                TreeNode curr=queue.poll();

                if (curr.left!=null && !visited.contains(curr.left)) {
                    visited.add(curr.left);
                    queue.offer(curr.left);
                }

                if (curr.right!=null && !visited.contains(curr.right)) {
                    visited.add(curr.right);
                    queue.offer(curr.right);
                }

                TreeNode parent=parentMap.get(curr);
                if (parent != null && !visited.contains(parent)) {
                    visited.add(parent);
                    queue.offer(parent);
                }
            }

            distance++;
        }

        return new ArrayList<>();
    }
}