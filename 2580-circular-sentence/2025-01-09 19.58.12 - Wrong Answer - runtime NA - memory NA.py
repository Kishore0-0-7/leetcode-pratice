class Solution(object):
    def isCircularSentence(self, sentence):
        words=sentence.split()
        if(len(words))==1:
            if not (words[0])[-1]==(words[0])[0]:
                return False
        for i in range(len(words)-1):
            if (words[i])[-1]!=(words[i+1])[0]:
                return False
        return True
        