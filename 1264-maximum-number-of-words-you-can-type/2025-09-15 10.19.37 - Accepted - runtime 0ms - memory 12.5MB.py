class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        lst=text.split(" ")
        bklist=set(brokenLetters)
        cnt=len(lst)
        for word in lst:
            for let in bklist:
                if let in word:
                    cnt-=1
                    break
        return cnt