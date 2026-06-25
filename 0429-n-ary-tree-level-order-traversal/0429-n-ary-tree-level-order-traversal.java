/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    List<List<Integer>> list=new ArrayList<>();
    public List<List<Integer>> levelOrder(Node root) {
        if(root==null) return list;
        Queue<Node> q=new LinkedList<>();
        q.add(root);
        while(!q.isEmpty()){
            List<Integer> lst=new ArrayList<>();
            int s=q.size();
            for(int i=0;i<s;i++){
                Node curr=q.poll();
                lst.add(curr.val);
                for(Node n:curr.children){
                    q.add(n);
                }
            }
            list.add(lst);
        }
        return list;
    }
}