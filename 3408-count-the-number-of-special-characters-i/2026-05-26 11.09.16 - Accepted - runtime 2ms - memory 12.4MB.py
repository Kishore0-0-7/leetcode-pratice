class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower_case=[False]*26
        upper_case=[False]*26
        for ch in word:
            if ch.isupper():
                upper_case[ord(ch)-ord('A')]=True
            else:
                lower_case[ord(ch)-ord('a')]=True
        result=0
        for i in range(26):
            if lower_case[i] and upper_case[i]:
                result+=1
        return result