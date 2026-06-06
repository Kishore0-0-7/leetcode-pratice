class Solution(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        cx,cy=center
        best_quality=-1
        best_coord=[-1,-1]
        for x, y, q in towers:
            dist=abs(x-cx)+abs(y-cy)
            if dist<=radius:
                if q>best_quality or (q==best_quality and [x,y]<best_coord):
                    best_quality=q
                    best_coord=[x,y]
        return best_coord