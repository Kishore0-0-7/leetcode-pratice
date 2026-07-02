class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans=new ArrayList<>();
        List<Integer> ds=new ArrayList<>();
        helper(0,target,candidates,ans,ds);
        return ans;
    }
    void helper(int idx,int target,int arr[],List<List<Integer>> ans,List<Integer> ds){
        if(target==0){
            ans.add(new ArrayList<>(ds));
            return;
        }
        for(int i=idx;i<arr.length;i++){
            if(i>idx&&arr[i]==arr[i-1]) continue;
            if(arr[i]>target) break;
            ds.add(arr[i]);
            helper(i+1,target-arr[i],arr,ans,ds);
            ds.remove(ds.size()-1);
            // helper(idx+1,target,arr,ans,ds);
        }
    }
}