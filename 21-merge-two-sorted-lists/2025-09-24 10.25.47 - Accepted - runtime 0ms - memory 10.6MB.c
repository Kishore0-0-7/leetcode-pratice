/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode t;
       struct ListNode* h=&t;
        while(list1 && list2){
            if(list1->val<list2->val){
                h->next=list1;
                list1=list1->next;
            }
            else{
                h->next=list2;
                list2=list2->next;
            }
            h=h->next;
        }
        h->next=(list1)?list1:list2;
        return t.next;
}