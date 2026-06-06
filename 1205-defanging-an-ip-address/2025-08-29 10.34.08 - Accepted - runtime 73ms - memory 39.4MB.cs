public class Solution {
    public string DefangIPaddr(string address) {
        return String.Join("[.]",address.Split("."));
    }
}