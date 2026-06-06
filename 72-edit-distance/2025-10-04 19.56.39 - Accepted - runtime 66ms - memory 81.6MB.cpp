class Solution {
public:
    int helper(string word1,string word2,int i,int j,int **dp)
    {
        if(i==word1.length()) return word2.length()-j;
        if(j==word2.length()) return word1.length()-i;
        if(dp[i][j]!=-1) return dp[i][j];
        int answer=0;
        if(word1[i]==word2[j])
        {
            answer=helper(word1,word2,i+1,j+1,dp);
        }
        else
        {
            int insertAnswer=1+helper(word1,word2,i,j+1,dp);
            int deleteAnswer=1+helper(word1,word2,i+1,j,dp);
            int replaceAnswer=1+helper(word1,word2,i+1,j+1,dp);
            answer=min({insertAnswer,deleteAnswer,replaceAnswer});
        }
        dp[i][j]=answer;
        return dp[i][j];
    }
    int minDistance(string word1, string word2) {
        int m=word1.length(); int n=word2.length();
        int **dp=new int*[m];
        for(int i=0; i<m; i++)
        {
            dp[i]=new int[n];
        }
        for(int i=0; i<m; i++)
        {
            for(int j=0; j<n; j++)
            {
                dp[i][j]=-1;
            }
        }
        return helper(word1,word2,0,0,dp);
    }
};
 