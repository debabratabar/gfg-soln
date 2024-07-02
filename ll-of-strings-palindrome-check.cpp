/*

Question Link : https://www.geeksforgeeks.org/problems/linked-list-of-strings-forms-a-palindrome/1
Question Name : linked list of strings forms a palindrome


*/

class Solution {
  public:
    bool compute(Node* head) {
        // Your code goes here
        string  result ;
        while(head!= nullptr){
            result += head->data;
            head= head->next ;
        }
        
        for ( int i =0 , j = result.length()-1   ; i< j ;i++,j--){
            if ( result[i] != result[j]){
                return false ;
            }
        }
     
    return true ;   
    }
    
    
};