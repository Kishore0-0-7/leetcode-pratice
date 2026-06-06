public class Solution {
    public int SecondHighest(string s) {
        HashSet<int> digits=new HashSet<int>();
        foreach (char c in s) {
            if (char.IsDigit(c)) {
                digits.Add(c-'0');
            }
        }
        if (digits.Count<=1) return -1;
        List<int> list=new List<int>(digits);
        list.Sort();
        return list[list.Count-2];
    }
}