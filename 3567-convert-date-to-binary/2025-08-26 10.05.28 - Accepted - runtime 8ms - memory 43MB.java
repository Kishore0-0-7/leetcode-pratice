class Solution {
    public String convertDateToBinary(String date) {
        String []datelist=date.split("-");
        String year=Integer.toBinaryString(Integer.parseInt(datelist[0]));
        String month=Integer.toBinaryString(Integer.parseInt(datelist[1]));
        String datetime=Integer.toBinaryString(Integer.parseInt(datelist[2]));
        return (year+"-"+month+"-"+datetime);
    }
}