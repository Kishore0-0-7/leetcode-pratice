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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode s=head,e=head;
        for(int i=0;e!=null && i<n;i++) e=e.next;
        
        if(e==null) return head.next;
        
        while(e.next!=null){
            e=e.next;
            s=s.next;
        }
        s.next=s.next.next;
        return head;
    }
}