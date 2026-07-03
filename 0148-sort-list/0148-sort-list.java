/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val=val; }
 *     ListNode(int val, ListNode next) { this.val=val; this.next=next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if(head==null||head.next==null) return head;
        ListNode m=mid(head);
        ListNode r=m.next;
        m.next=null;
        ListNode l=head;
        l=sortList(l);
        r=sortList(r);
        return merge(l,r);
    }
    ListNode mid(ListNode head){
        if(head==null||head.next==null) return head;
        ListNode s=head,f=head.next;
        while(f!=null&&f.next!=null){
            f=f.next.next;
            s=s.next;
        }
        return s;
    }
    ListNode merge(ListNode l1,ListNode l2){
        ListNode dummyNode=new ListNode(0);
        ListNode temp=dummyNode;
        while (l1!=null && l2!=null) {
            if (l1.val <= l2.val) {
                temp.next=l1;
                l1=l1.next;
            } else {
                temp.next=l2;
                l2=l2.next;
            }
            temp=temp.next;
        }
        if (l1!=null) {
            temp.next=l1;
        } else {
            temp.next=l2;
        }
        return dummyNode.next;    
    }
}