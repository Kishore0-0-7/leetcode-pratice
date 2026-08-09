class Solution {
    public long weightedSum(int[] parent, int[] nums) {
        int n=parent.length;
        List<List<Integer>> child=new ArrayList<>();
        for(int i=0;i<n;i++){
            child.add(new ArrayList<>());
        }
        for(int i=1;i<n;i++){
            child.get(parent[i]).add(i);
        }
 int[] depth=new int[n];
        Queue<Integer> q=new LinkedList<>();
        depth[0]=1;
        q.add(0);
        int h=1;
        while(!q.isEmpty()){
            int node=q.poll();
            for(int c:child.get(node)){
                depth[c]=depth[node]+1;
                h=Math.max(h,depth[c]);
                q.add(c);
            }
        }
        long ans=0;
        for(int i=0;i<n;i++){
            long w=(long) nums[i] *(h-depth[i]+1);
            ans+=w;
        }
        return ans;
    }
}