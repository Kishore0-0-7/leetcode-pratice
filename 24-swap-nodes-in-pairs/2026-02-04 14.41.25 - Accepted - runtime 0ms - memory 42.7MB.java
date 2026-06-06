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
    public ListNode swapPairs(ListNode head) {
        if(head==null || head.next==null) return head;
        ListNode t=new ListNode(0);
        t.next=head;
        ListNode d=t;
        while(d.next!=null && d.next.next!=null){
            ListNode f=d.next;
            ListNode s=d.next.next;
            d.next=s;
            f.next=s.next;
            s.next=f;
            d=d.next.next;
        }
        return t.next;
    }
}