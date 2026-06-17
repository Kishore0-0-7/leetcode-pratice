class Solution {
    public int majorityElement(int[] nums) {
        int n=nums.length,cnt=0,el=0;
        for(int i=0;i<n;i++){
            if(cnt==0){
                cnt+=1;
                el=nums[i];
            }
            else if(nums[i]==el) cnt++;
            else cnt--;
        }

        return el;
    }
}