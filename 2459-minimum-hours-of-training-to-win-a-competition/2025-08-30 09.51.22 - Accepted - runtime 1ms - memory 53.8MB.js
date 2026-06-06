/**
 * @param {number} initialEnergy
 * @param {number} initialExperience
 * @param {number[]} energy
 * @param {number[]} experience
 * @return {number}
 */
var minNumberOfHours = function(initialEnergy, initialExperience, energy, experience) {
        let ans=0;
        for (let i=0;i<energy.length;i++){
            while(initialEnergy <=energy[i] || initialExperience<=experience[i]){
                if (initialEnergy <= energy[i]){
                    initialEnergy+=1;
                    ans+=1;
                }
                if (initialExperience<=experience[i]){
                    initialExperience+=1;
                    ans+=1;
                }
            }
            initialEnergy-=energy[i];
            initialExperience+=experience[i];
        }
        return ans;
};