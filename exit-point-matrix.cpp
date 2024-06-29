/*

Question Link : https://www.geeksforgeeks.org/problems/exit-point-in-a-matrix0905/1

*/ 
  
  
  
  
  
  class Solution{
  public:
  vector<int> FindExitPoint(int n, int m, vector<vector<int>>& matrix) {
        // Code here
        
        // 1. if prev & curr is in same row but prev is smaller col then we will move next row same col 
        
        // 2. !1 -->  prev row same col 
        
        // 3. if prev & curr is in same col and prev is smaller row then we will move prev col same row 
        // 4. !3 --> next col same row 
        
        // until row < n or col <m
        
        // for every run we will record previous index  & current index 
        vector<int> prev(2,0);
        vector<int> curr(2,0);
        
        int i=0, j =0 ;
        
        // updatinf prev & curr for first element 
        if ( matrix[0][0] == 0 ){
            curr[0] = 0 ;
            curr[1] = 1 ;
            i=0;
            j = 1 ; 
        }
        else{
            curr[0] = 1 ;
            curr[1] = 0 ;
            i=1;
            j = 0 ; 
            matrix[0][0] = 0;
        }
        
        
        while (  (i< n && i>=0 )  && (j<m &&  j>=0 ) ){
            
            // path for 1 
            if (matrix[i][j]==1){
            
                if ( prev[0] == curr[0]  ){
                    if (prev[1] < curr[1] ){
                        i++;
                    }
                    else{
                        i--;
                    }
                    prev[0] = curr[0];
                    prev[1] = curr[1];
                    curr[0] = i; 
                }
                else if (prev[1] == curr[1] ){
                    if( prev[0] < curr[0]  ){
                        j--;
                    }
                    else{
                        j++;
                    }
                    prev[0] = curr[0];
                    prev[1] = curr[1];
                    curr[1] = j; 
                }
                else{
                    
                }
                // updating 1 -> 0 
            matrix[prev[0]][prev[1]] = 0 ; 
            }
            //path for 0 
            else{
                if ( prev[0] == curr[0]  ){
                    if (prev[1] < curr[1] ){
                    j++;
                    }
                    else{
                         j--;
        
                    }
                prev[0] = curr[0];
                prev[1] = curr[1];
                curr[1] = j; 
                }
                else if (prev[1] == curr[1] ){
                    if( prev[0] < curr[0]  ){
                         i++;
                        }
                    else{
                        i--;
                    }
                    prev[0] = curr[0];
                    prev[1] = curr[1];
                    curr[0] = i; 
                }
                else{
    
                    }

                
            }
            
           
        }
         // fix the exit index as it incresed or decresed by 1 when exiting from last loop
        if (curr[0] < 0 ){
            curr[0]++;
        }
        if (curr[1] < 0 ){
            curr[1]++;
        }
        if (curr[0] >= n ){
            curr[0]--;
        }
        if (curr[1] >=m  ){
            curr[1]--;
        }
        
            
            return curr ; 
  }

};