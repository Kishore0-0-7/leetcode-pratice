public class Solution {
    public bool IsValid(string word) {
        if (word.Length < 3) return false;
        int vowels=0, consonants=0;
        foreach (char c in word) {
            if (Char.IsLetter(c)) {
                if ("aeiouAEIOU".Contains(c)) {
                    vowels++;
                } else {
                    consonants++;
                }
            } else if (!Char.IsDigit(c)) {
                return false;
            }
        }
        return vowels>=1 && consonants>=1;
    }
}