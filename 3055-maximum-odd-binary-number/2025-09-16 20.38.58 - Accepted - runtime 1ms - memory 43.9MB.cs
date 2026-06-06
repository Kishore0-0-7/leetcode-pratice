public class Solution {
    public string MaximumOddBinaryNumber(string s) {
        char[] arr = s.ToCharArray();
        int ones = 0;
        for (int i=0;i<arr.Length;i++) {
            if (arr[i]=='1') {
                arr[i]='0';
                ones++;
            }
        }
        for (int i=0;i<ones-1;i++) {
            arr[i]='1';
        }
        arr[arr.Length-1]='1';
        return new string(arr);
    }
}