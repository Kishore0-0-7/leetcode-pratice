class Solution(object):
    def trafficSignal(self, timer):
        """
        :type timer: int
        :rtype: str
        """
        if timer==0:
            return "Green"
        if timer==30:
            return "Orange"
        if timer>30 and timer<=90:
            return "Red"
        return "Invalid"