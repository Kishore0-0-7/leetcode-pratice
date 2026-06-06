class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(words) != len(pattern):
            return False
        charWord = {}
        wordChar = {}
        for ch, word in zip(pattern, words):
            if ch in charWord and charWord[ch] != word:
                return False
            elif word in wordChar and wordChar[word] != ch:
                return False
            else:
                charWord[ch] = word
                wordChar[word] = ch
        return True