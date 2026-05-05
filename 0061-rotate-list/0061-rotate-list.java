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
    public ListNode rotateRight(ListNode head, int k) {
        if(head==null || head.next==null || k==0) return head;
        int c=1;
        ListNode t=head,h=head;
        for(c=1;t.next!=null;c++) t=t.next;
        int n=c-k%c;
        for(int i=0;i<n-1;i++){ 
            System.out.print(h.val);
            h=h.next;
            }
        t.next=head;
        head=h.next;
        h.next=null;
        return head;
    }
}