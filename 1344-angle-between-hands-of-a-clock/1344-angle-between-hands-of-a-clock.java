class Solution {
    public double angleClock(int hour, int minutes) {
        double mi=6.0*minutes;
        double hr=30.0*(hour%12)+0.5*minutes;
        double dif=Math.abs(hr-mi);
        return Math.min(dif,360-dif);
    }
}