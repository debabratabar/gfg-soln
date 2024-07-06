
/*

Question Link : https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
Question Name : Reverse Words

*/


class Solution
{
    public:
    //Function to reverse words in a given string.
    string reverseWords(string S) 
    { 
        // code here 
        // int firstPtr= ;
        string result ;
        
        int count  = 0 ;
        for ( int i = S.size()-1;i>=0;i--){
            // cout << S[i] << " " ;
            if( S[i]=='.'){
                //  cout << S[i] << " " ;
                string temp = S.substr(i+1 , count);
                // cout << temp ;
                result+=temp+'.';
                count=0;
            }
            else{
                count++;
            }
        }
        for ( int i =0;S[i]!='.' && i<S.size();i++){
            result+=S[i];
        }
        
        // cout << endl << result;
        
        return result ;
    } 
};