/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        //Create Dummy Node
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;

        ListNode* curr = dummy;
        while(curr->next){
            //Check Value
            if(curr->next->val == val){
                curr->next = curr->next->next;
            }else{
                curr = curr->next;
            }
        } 
        //return head
        return dummy->next;
    }
};

/*1->2->6->3->4->5->6
dummy = head
1. dummy->1->2->6->3->4->5->6
curr = dummy
-  1 not equal val, curr = cur->next  
-  2 not equal val, curr = cur->next
-  6 is equal val, curr = cur->next->next (removed)
-  3 not equal val, curr = cur->next
-  4 not equal val, curr = cur->next
-  5 not equal val, curr = cur->next
-  6 is equal val, curr = cur->next->next (removed)

dummy->next = [1,2,3,4,5]
*/
