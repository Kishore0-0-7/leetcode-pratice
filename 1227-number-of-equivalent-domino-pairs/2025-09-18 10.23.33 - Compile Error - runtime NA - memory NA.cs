public class Solution {
    public int NumEquivDominoPairs(int[][] dominoes) {
        Dictionary<int,int> mp=new Dictionary<int,int>();
        int count=0;
        foreach (var d in dominoes) {
            int a=d[0],b=d[1];
            int key=Math.Min(a,b)*10+Math.Max(a,b);
            if (mp.ContainsKey(key)) {
                count+=mp[key];
                mp[key]++;
            } else {
                mp[key]=1;
            }
        }
    }
}