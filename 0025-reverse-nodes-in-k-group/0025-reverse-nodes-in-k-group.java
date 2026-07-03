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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode d=new ListNode(0);
        d.next=head;
        ListNode gp=d;
        while(true){
            ListNode kth=getkth(gp,k);
            if(kth==null) break;
            ListNode gn=kth.next;
            ListNode prev=gn;
            ListNode curr=gp.next;
            for(int i=0;i<k;i++){
                ListNode t=curr.next;
                curr.next=prev;
                prev=curr;
                curr=t;
            }
            ListNode temp=gp.next;
            gp.next=kth;
            gp=temp;
        }
        return d.next;
    }
    ListNode getkth(ListNode gp,int k){
        while(gp!=null&&k>0){
            gp=gp.next;
            k--;
        }
        return gp;
    }
}