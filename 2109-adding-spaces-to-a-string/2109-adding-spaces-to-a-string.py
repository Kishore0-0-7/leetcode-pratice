class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        arr=[]
        prev=0
        for space in spaces:
            arr.append(s[prev:space])
            prev=space
        arr.append(s[prev:])
       
        return " ".join(arr)