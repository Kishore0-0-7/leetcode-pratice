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
    class Pair{
        int h,l;
        TreeNode node;
        Pair(TreeNode n,int height,int level){
            node=n;
            h=height;
            l=level;
        }
    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        if (root == null) return new ArrayList<>();
      TreeMap<Integer,TreeMap<Integer,PriorityQueue<Integer>>> map=new TreeMap<>();
      Queue<Pair> q=new LinkedList<>();
      q.add(new Pair(root,0,0));
      while(!q.isEmpty()){
            Pair curr=q.poll();
            int x=curr.h;
            int y=curr.l;
            map.putIfAbsent(x,new TreeMap<>());
            map.get(x).putIfAbsent(y,new PriorityQueue<>());
            map.get(x).get(y).add(curr.node.val);
            if(curr.node.left!=null) q.add(new Pair(curr.node.left,x-1,y+1));
            if(curr.node.right!=null) q.add(new Pair(curr.node.right,x+1,y+1));
        }
        List<List<Integer>> ans=new ArrayList<>();
        for(TreeMap<Integer,PriorityQueue<Integer>> m:map.values()){
            List<Integer> list=new ArrayList<>();
            for(PriorityQueue<Integer> i:m.values()){
                while(!i.isEmpty())
                list.add(i.poll());
            }
            ans.add(list);
        }
        return ans;
      }
    }