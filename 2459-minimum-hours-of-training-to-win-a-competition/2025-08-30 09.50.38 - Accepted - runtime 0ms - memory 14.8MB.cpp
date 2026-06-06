class Solution {
public:
    int minNumberOfHours(int initialEnergy, int initialExperience, vector<int>& energy, vector<int>& experience) {
        int ans=0;
        for (int i=0;i<energy.size();i++){
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
    }
};