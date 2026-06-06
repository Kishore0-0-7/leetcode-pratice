class Solution(object):
    def detectCapitalUse(self, word):
        if len(word)<=1:
            return True
        return word.isupper() or word.islower()
        