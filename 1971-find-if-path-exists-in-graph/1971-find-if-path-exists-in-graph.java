class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> graph=new ArrayList<>();
        for(int i=0;i<n;i++) graph.add(new ArrayList<>());
        for(int[] edge:edges){
            int u=edge[0];
            int v=edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        boolean visited[]=new boolean[n];
        return dfs(source,destination,graph,visited);
    }
    boolean dfs(int node ,int dest,List<List<Integer>> graph,boolean[] visited){
        if(node==dest) return true;
        visited[node]=true;
        for(int neighbour:graph.get(node)){
            if(!visited[neighbour])
            if(dfs(neighbour,dest,graph,visited))
            return true;
        }
        return false;
    }
}