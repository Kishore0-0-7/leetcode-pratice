public class Solution {
    public int NumOfStrings(string[] patterns, string word) {
        int cnt=0;
        foreach(String w in patterns){
            if (word.Contains(w)) cnt+=1;
        }
        return cnt;
    }
}