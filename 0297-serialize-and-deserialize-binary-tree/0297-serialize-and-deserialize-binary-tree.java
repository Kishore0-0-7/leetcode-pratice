/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb=new StringBuilder();
        dfs(root,sb);
        return sb.toString();
    }   
    void dfs(TreeNode root,StringBuilder sb){
        if(root==null) {
            sb.append("N,");
            return;
        }
        sb.append(root.val).append(",");
        dfs(root.left,sb);
        dfs(root.right,sb);    
        }
    

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> q=new LinkedList<>();
        String[] arr=data.split(",");
        for(int i=0;i<arr.length;i++){
            q.add(arr[i]);
        }
        return build(q);
    }
    TreeNode build(Queue<String> q){
        String v=q.poll();
        if(v.equals("N")) return null;
        TreeNode root=new TreeNode(Integer.parseInt(v));
        root.left=build(q);
        root.right=build(q);
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));