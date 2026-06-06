class Solution(object):
    def isCircularSentence(self, sentence):
        words=sentence.split()
        for i in range(len(words)-1):
            if (words[i])[-1]!=(words[i+1])[0]:
                return False
        return True
        