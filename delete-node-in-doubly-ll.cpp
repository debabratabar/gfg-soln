/*

Question Link : https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1


*/



class Solution {
  public:
    Node* deleteNode(Node* head, int x) {
        // Your code here
        
        if ( x==1){
            head = head->next;
            head->prev = 0;
            
            return head ; 
        }
        
        Node* result = head ;
        int counter = 1;
        
        while(counter<x){
            head= head->next;
            counter++;
        }
        
        head = head->prev ;
        if( head->next->next == 0 ){
         head->next = 0 ;   
        }
        else{
        head->next = head->next->next;
        head->next->prev = head;
        }
        
        
        
        return result ;
        
        
    }
};