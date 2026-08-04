class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        Arrays.sort(nums);
        int ind=0;
        List<Integer> list=new ArrayList<>();
        for(int i=nums[0];i<nums[nums.length-1]+1;i++) 
        if(i==nums[ind]) ind++;
        else list.add(i);
        return list;
    }
}