class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        targetInt=ord(target)
        res_char=''
        for ch in letters:
            if ord(ch)>targetInt:
                res_char=ch
                break
        if not res_char:
            return letters[0]
        return res_char