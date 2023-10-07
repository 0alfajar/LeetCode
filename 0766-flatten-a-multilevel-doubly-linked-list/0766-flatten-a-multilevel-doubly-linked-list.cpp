/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        if(head == NULL) return head;
        Node* p = head;
        while(p){
            //case1: if no child
            if(p->child == NULL){
                p = p->next;
                continue;
            }
            //case 2: got child, find the tail of the child and link it to p->next
            Node* temp = p->child;
            //find tail of child
            while(temp->next){
                temp = temp->next;
            }
            //connect tail with p->next, if it is not null
            temp->next = p->next;
            if(p->next) p->next->prev = temp;
            //connect p with p->child, and remove p->child
            p->next = p->child;
            p->child->prev = p;
            p->child = NULL;
        }
        return head;
    }
};