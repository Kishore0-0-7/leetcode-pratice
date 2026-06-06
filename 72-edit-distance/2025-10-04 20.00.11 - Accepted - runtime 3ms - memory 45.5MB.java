class Solution {
    public int minDistance(String word1,String word2) {
        int m=word1.length();
        int n=word2.length();
        int[][] dp=new int[m][n];
        for (int i=0;i<m;i++) {
            Arrays.fill(dp[i],-1);
        }

        return helper(word1,word2,0,0,dp);
    }

    private int helper(String word1,String word2,int i,int j,int[][] dp) {
        if (i==word1.length()) return word2.length() - j;
        if (j==word2.length()) return word1.length() - i;

        if (dp[i][j] != -1) return dp[i][j];

        int ans;
        if (word1.charAt(i)==word2.charAt(j)) {
            ans=helper(word1,word2,i+1,j+1,dp);
        } else {
            int insertAns=1+helper(word1,word2,i,j+1,dp);
            int deleteAns=1+helper(word1,word2,i+1,j,dp);
            int replaceAns=1+helper(word1,word2,i+1,j+1,dp);
            ans=Math.min(insertAns,Math.min(deleteAns,replaceAns));
        }
        dp[i][j]=ans;
        return ans;
    }
}