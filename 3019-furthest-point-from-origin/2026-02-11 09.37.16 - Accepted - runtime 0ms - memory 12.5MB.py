class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        lc,rc,dc=0,0,0
        for c in moves:
            if c=="L":
                lc+=1
            elif c=="R":
                rc+=1
            else:
                dc+=1
        return abs(rc-lc)+dc