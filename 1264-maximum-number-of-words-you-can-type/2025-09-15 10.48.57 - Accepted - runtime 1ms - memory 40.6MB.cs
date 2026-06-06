public class Solution {
    public int CanBeTypedWords(string text, string brokenLetters) {
        string[] words = text.Split(' ');
        int count = words.Length;
        foreach (string word in words) {
            foreach (char ch in brokenLetters) {
                if (word.Contains(ch)) {
                    count--;
                    break;
                }
            }
        }
        return count;
    }
}