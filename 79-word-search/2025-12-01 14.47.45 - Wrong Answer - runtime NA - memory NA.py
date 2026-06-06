class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        d={}
        for _ in board:
            for c in _:
                d[c]=d.get(c,0)+1
        for ch in word:
            if d.get(ch,0)<=0:
                return False
            d[ch]=d.get(ch)-1
        return True