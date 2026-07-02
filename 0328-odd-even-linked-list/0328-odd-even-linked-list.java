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
    public ListNode oddEvenList(ListNode head) {
        ListNode evenHead=null,evenTail=null;
        ListNode oddHead=null,oddTail=null;
        ListNode t=head;
        int i=1;
        while(t!=null){
            if(i++%2==0){
                if(evenHead==null){
                    evenHead=t;
                    evenTail=t;
                }
                else{
                    evenTail.next=t;
                    evenTail=evenTail.next;
                }
            }
            else{
                if(oddHead==null){
                    oddHead=t;
                    oddTail=t;
                }
                else{
                    oddTail.next=t;
                    oddTail=oddTail.next;
                }
            }
            t=t.next;            
        }
        if(oddHead==null) return evenHead;
        if(evenHead==null) return oddHead;
        oddTail.next=evenHead;
        evenTail.next=null;
        return oddHead;
    }
}