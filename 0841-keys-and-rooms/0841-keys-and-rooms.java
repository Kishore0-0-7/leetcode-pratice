class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
       boolean[] visited=new boolean[rooms.size()];
       dfs(0,rooms,visited);
       for(boolean f:visited)
       if(!f) return false;
       return true;
    }
    void dfs(int ind,List<List<Integer>> rooms,boolean[] visited){
        visited[ind]=true;
        for(int neigh:rooms.get(ind)) {
            if(!visited[neigh]) dfs(neigh,rooms,visited);
        }
    }
}