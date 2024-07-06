/*

Question Link : https://www.geeksforgeeks.org/problems/reverse-a-string/
Question Name : Reverse a string


*/



class Solution
{
    public:
    string reverseWord(string str)
    {
        // Your code goes here
         for ( int i = 0 , j=str.size()-1 ; i<j ; i++,j--){
            swap(str[i] , str[j]);
        }
        
        string result  = str; 
        
        return result; 
    }
};