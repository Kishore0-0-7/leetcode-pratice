class Solution {
    public int numSplits(String s) {
        int lf[]=new int[26];
        int rf[]=new int[26];
        int rd=0;
        for(char ch:s.toCharArray()) {
            if(rf[ch-'a']==0) rd++;
            rf[ch-'a']++;
        }
        int ans=0,ld=0;
        for(int i=0;i<s.length()-1;i++){
            int idx=s.charAt(i)-'a';
            if(lf[idx]++==0) ld++;
            // lf[idx]++;

            // rf[idx]--;
            if(--rf[idx]==0) rd--;
            
            if(ld==rd) ans++;
        }
        return ans;
    }
}