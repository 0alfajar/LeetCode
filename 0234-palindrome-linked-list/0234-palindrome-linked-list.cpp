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
    bool isPalindrome(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;

        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        ListNode* curr = slow;
        ListNode* prev = NULL;
        ListNode* next = NULL;
        while(curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        ListNode* low = head;
        ListNode* high = prev;
        while(high){
            if(high->val != low->val){
                return false;
            }
            low = low->next;
            high = high->next;
        }
        return true;
    }
};