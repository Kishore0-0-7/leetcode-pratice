class Solution {
    public int numberOfUniqueGoodSubsequences(String binary) {
        int MOD=1_000_000_007;
        int e0=0,e1=0;
        boolean h0=false;
        for(char ch:binary.toCharArray()){
            if(ch=='0'){
                h0=true;
                e0=(e0+e1)%MOD;
            }
            else e1=(e0+e1+1)%MOD;
        }
        return h0?(e0+e1+1)%MOD:(e0+e1)%MOD;
    }
}