int minNumberOfHours(int initialEnergy, int initialExperience, int* energy, int energySize, int* experience, int experienceSize) {
    int ans=0;
        for (int i=0;i<energySize;i++){
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