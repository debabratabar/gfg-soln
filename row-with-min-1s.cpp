/*

Question Link : https://www.geeksforgeeks.org/problems/row-with-minimum-number-of-1s5430/1

*/

class Solution {
  public:
    int minRow(int n, int m, vector<vector<int>> a) {
        // code here
        
        int resultRow = 0 ;
        int minCount =INT_MAX;
        int count =0;
        for  ( int i=0 ; i<n ;i++){
            count =0;
            for ( int j = 0 ;j<m;j++){
                if(a[i][j] == 1 ){
                    count++;
                }
            }
            
            // cout << count << " " ;
            if ( count < minCount ){
                resultRow = i+1;
                minCount = count ;
            }
            // cout << resultRow << " " ;
        }
        
        return resultRow ; 
    }
};