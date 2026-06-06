class Solution(object):
    def squareIsWhite(self, c):
        """
        :type coordinates: str
        :rtype: bool
        """
        if c[0] in 'aceg':
            return int(c[1])%2==0
        elif c[0] in 'bdfh':
            return int(c[1])%2==1
        return False