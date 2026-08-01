class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> ans=new ArrayList<>();
        dfs(0,graph,ans,new ArrayList<>());
        return ans;
    }
    void dfs(int node,int[][] graph,List<List<Integer>> ans,List<Integer> cur){
        cur.add(node);
        if(node==graph.length-1) ans.add(new ArrayList<>(cur));
        else{
            for(int neigh:graph[node])
            dfs(neigh,graph,ans,cur);
        }
        cur.remove(cur.size()-1);
    }
}