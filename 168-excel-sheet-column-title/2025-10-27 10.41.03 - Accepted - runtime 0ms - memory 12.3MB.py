class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        s=""
        while(columnNumber>0):
            columnNumber-=1
            s=chr((columnNumber%26)+ord('A'))+s
            columnNumber=columnNumber//26
        return s