public class Solution {
    public int RemovePalindromeSub(string s) {
        if (s=="") return 0;
        char[] revarray=s.ToCharArray();
        Array.Reverse(revarray);
        string rev=new string(revarray);
        if (s==rev) return 1;
        else return 2;
    }
}