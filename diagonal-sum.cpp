/*

Question Link : https://www.geeksforgeeks.org/problems/diagonal-sum0158/1


*/


class Solution {
public:
    int DiagonalSum(vector<vector<int> >& matrix) {
        // Code here
        int sum = 0 ;
        int n = matrix.size();
        //left diagonal
        for ( int i =0;i<n;i++){
                    sum+=matrix[i][i];
                }

        //right diagonal
        for ( int i =0, j =n-1;i<n;i++, j-- ){
                    sum+=matrix[i][j];
                }
        
        return sum ;
    }
};