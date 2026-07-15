class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans=new ArrayList<>();
        helper(0,nums,ans,new ArrayList<>());
        return ans;
    }
    void helper(int start,int[] nums,List<List<Integer>> ans,List<Integer> cur){
        ans.add(new ArrayList<>(cur));
        for(int i=start;i<nums.length;i++){
            cur.add(nums[i]);
            helper(i+1,nums,ans,cur);
            cur.remove(cur.size()-1);
        }
    }
}