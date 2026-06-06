class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target=abs(target)
        steps,moves = 0, 0
        while steps < target or (steps-target) % 2 != 0:
            moves+=1
            steps+=moves
        return moves
