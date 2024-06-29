/*

Question Link : https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1


*/



class Solution{
public:
	int rowWithMax1s(vector<vector<int> > arr, int n, int m) {
	    // code here
	    
        // we are traversing col by col | col1 -> col2 -> col..
        // as rows are sorted , when we get first 1 that will be our ans 
	    int i=0,j=0;
	    for( ; i<n && j<m;i++){
	       // cout << i<< " " << j  << endl ;
	        if ( arr[i][j] == 1 ){
	            return i;
	        }
	        
	        if ( i == n-1 ){
	            i=-1;
	            j++;
	        }
	        
	    }
	    return -1 ;
	}

};