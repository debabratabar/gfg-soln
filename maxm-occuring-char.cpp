/*

Question Link : https://www.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1
Question Name : Maximum Occuring Character 

*/ 

class Solution
{
    public:
    //Function to find the maximum occurring character in a string.
    char getMaxOccuringChar(string str)
    {
        // Your code here
        vector<int> freq(26,0);
        
        
        for ( int i = 0;i<str.size();i++){
            freq[str[i]-97]++;
        }
        
        int max= INT_MIN ;
        for ( int i=0;i<freq.size();i++){
            if ( freq[i] > max){
                max= freq[i] ;
            }
        }
        
        
        char result ;
        for ( int i=0;i<freq.size();i++){
            if(freq[i] == max){
                result=char(i+97);
                break ;
            }
        }
        
        return result ; 
    }

};