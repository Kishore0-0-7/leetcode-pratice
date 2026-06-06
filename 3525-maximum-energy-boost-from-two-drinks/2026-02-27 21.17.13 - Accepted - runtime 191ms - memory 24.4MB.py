class Solution(object):
    def maxEnergyBoost(self, energyDrinkA, energyDrinkB):
        """
        :type energyDrinkA: List[int]
        :type energyDrinkB: List[int]
        :rtype: int
        """
        pa2=0
        pa1=0
        pb2=0
        pb1=0
        L=len(energyDrinkA)
        for i in range(L):
            ca=max(pa1,pb2)+energyDrinkA[i]
            cb=max(pb1,pa2)+energyDrinkB[i]
            pa2=pa1
            pb2=pb1
            pa1=ca
            pb1=cb
        return max(ca,cb)