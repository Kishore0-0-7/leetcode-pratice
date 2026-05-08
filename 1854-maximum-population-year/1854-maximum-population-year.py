class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        totalYears=2050-1950+1
        population=[0]*totalYears
        for log in logs:
            birthYear=log[0]
            deathYear=log[1]
            population[birthYear-1950]+=1
            population[deathYear-1950]-=1
        currPop=maxPop=result=0
        for year in range(totalYears):
            currPop+=population[year]
            if currPop>maxPop:
                maxPop=currPop
                result=year
        return result+1950