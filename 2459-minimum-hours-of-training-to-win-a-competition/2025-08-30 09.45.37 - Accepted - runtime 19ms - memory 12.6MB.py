class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        ans=0
        for i in range(len(energy)):
            while initialEnergy <=energy[i] or initialExperience<=experience[i]:
                if initialEnergy <= energy[i]:
                    initialEnergy+=1
                    ans+=1
                if initialExperience<=experience[i]:
                    initialExperience+=1
                    ans+=1
            initialEnergy-=energy[i]
            initialExperience+=experience[i]
        return ans