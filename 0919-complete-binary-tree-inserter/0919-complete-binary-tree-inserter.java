/**
 * Definition for a binary tree node.
 * public class TreeNode{
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(){}
 *     TreeNode(int val){ this.val=val; }
 *     TreeNode(int val, TreeNode left, TreeNode right){
 *         this.val=val;
 *         this.left=left;
 *         this.right=right;
 *     }
 * }
 */

class CBTInserter{

    Queue<TreeNode> q=new LinkedList<>();
    TreeNode root;

    public CBTInserter(TreeNode root){
        this.root=root;
        q.add(root);
        while (true){
            TreeNode node=q.peek();
            if (node.right!=null){
                q.remove();
                q.add(node.left);
                q.add(node.right);
            } else{
                if (node.left!=null) q.add(node.left);
                break;
            }
        }
    }

    public int insert(int val){
        TreeNode node=new TreeNode(val);
        if (q.peek().left==null){
            q.peek().left=node;
        } else if (q.peek().right==null){
            q.peek().right=node;
        } else{
            q.remove();
            q.peek().left=node;
        }
        q.add(node);
        return q.peek().val;
    }

    public TreeNode get_root(){
        return root;
    }

}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj=new CBTInserter(root);
 * int param_1=obj.insert(val);
 * TreeNode param_2=obj.get_root();
 */