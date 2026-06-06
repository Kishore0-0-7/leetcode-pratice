/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        ListNode s=head;
        ListNode f=head;
        while(f!=null&&f.next!=null){
            s=s.next;
            f=f.next.next;
        }
        ListNode prev=null;
        ListNode next=null;
        while(s!=null){
            next=s.next;
            s.next=prev;
            prev=s;
            s=next;
        }
        int sum=0;
        while(prev!=null){
            sum=Math.max(sum,head.val+prev.val);
            head=head.next;
            prev=prev.next;
        }
            return sum;
        
        
    }
}