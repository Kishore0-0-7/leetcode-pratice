public class Solution {
    public char KthCharacter(int k) {
         StringBuilder sb=new StringBuilder("a");
        while (sb.Length<k) {
            int size=sb.Length;
            for (int i=0;i<size;i++) {
                char c=sb[i];
                sb.Append((char)('a'+((c-'a'+1)%26)));
            }
        }
        return sb[k-1];
    }
}