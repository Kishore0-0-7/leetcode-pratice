class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        Map <Integer, Integer> map=new HashMap<>();
        int res = 0, i = 0, n = nums.length;
        for (int j = 0; j < n; ++j) {   
            map.put(nums[j],map.getOrDefault(nums[j],0)+1);
            while(map.get(nums[j])>k)
            map.put(nums[i],map.get(nums[i++])-1);
            res = Math.max(res,j-i+1);
        }
        return res;
    }
}