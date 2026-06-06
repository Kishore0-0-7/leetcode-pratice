class Solution(object):
    def minMoves(self, balance):
        """
        :type balance: List[int]
        :rtype: int
        """
        n=len(balance)
        total=sum(balance)

        if total<0:
            return -1
        neg=-1
        for i in range(n):
            if balance[i]<0:
                neg=i
                break
        if neg==-1: return 0
        need=-balance[neg]
        moves=0
        for d in range(1,n+1):
            if need==0:
                break
            l=(neg-d)%n
            r=(neg+d)%n
            if l==r:
                take=min(balance[l],need)
                if take>0:
                    balance[l]-=take
                    need-=take
                    moves+=take*d
            else:
                takel=min(balance[l],need)
                if takel>0:
                    balance[l]-=takel
                    need-=takel
                    moves+=takel*d
                taker=min(balance[r],need)
                if taker>0:
                    balance[r]-=taker
                    need-=taker
                    moves+=taker*d
        return moves if need==0 else -1