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
    public ListNode partition(ListNode head, int x) {
        ListNode lh=new ListNode(0),gh=new ListNode(0);
        ListNode lt=lh,gt=gh,t=head;
        while(t!=null){
            if(t.val<x){
                lt.next=t;
                lt=lt.next;
            }
            else{
                gt.next=t;
                gt=gt.next;
            }
            t=t.next;
        }
        gt.next=null;
        if(lh.next==null) return gh.next;
        lt.next=gh.next;
        return lh.next;
    }
}