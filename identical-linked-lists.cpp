/*

Question Link : https://www.geeksforgeeks.org/problems/identical-linked-lists/1


*/


bool areIdentical(struct Node *head1, struct Node * head2) {
    // Code here
    
    Node *ll1 = head1;
    Node *ll2 = head2;
    
    int ll1_size = 0;
    int ll2_size = 0;
    while(ll1!=NULL){
        ll1_size++;
        ll1= ll1->next;
    }
    
    while(ll2!=NULL){
        ll2_size++;
        ll2= ll2->next;
    }

    // checking the size of two linked list    , if not match then return false 
    if ( ll1_size != ll2_size ){
        return false ;
    }
    

    ll1 = head1;
    ll2 = head2;
    
    
    while( ll1 != NULL || ll2 != NULL ){
        if( ll1->data != ll2->data ){
            return false ;
        }
        ll1= ll1->next;
        ll2= ll2->next;
    }
    
    return true ; 
    
}