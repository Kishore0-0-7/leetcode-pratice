class Solution {
    public int scoreDifference(int[] nums) {
        int a11=0;
        int b11=0;
        boolean a1=true;
        for(int i=0;i<nums.length;i++){
            if(nums[i]%2!=0){
                a1=!a1;
            }
            if(i%6==5){
                a1=!a1;
            }
            if(a1){
                a11+=nums[i];
            }
            else{
                b11+=nums[i];
            }
        }
        return a11-b11;
        }
    }
       