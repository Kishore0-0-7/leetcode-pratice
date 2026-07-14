class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> ans=new ArrayList<>();
        solve(0,nums,ans);
        return ans;
    }
    void solve(int index,int[] nums,List<List<Integer>> ans){
        if(index==nums.length){
            List<Integer> list=new ArrayList<>();
            for(int i:nums) list.add(i);
            ans.add(list);
            return;
        }
        for(int i=index;i<nums.length;i++){
            swap(nums,index,i);
            solve(index+1,nums,ans);
            swap(nums,index,i);
        }
    }
    void swap(int nums[],int a,int b){
        int t=nums[a];
        nums[a]=nums[b];
        nums[b]=t;
    }
}