/*

Question Link : https://www.geeksforgeeks.org/problems/last-cell-in-a-matrix/1


*/

class Solution{
    public:
    pair<int,int> endPoints(vector<vector<int>> matrix, int R, int C){
        //code here
        
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
        
        
        while (  (i< R && i>=0 )  && (j<C &&  j>=0 ) ){
            
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
        if (curr[0] >= R ){
            curr[0]--;
        }
        if (curr[1] >=C  ){
            curr[1]--;
        }
        
        pair<int,int> result ;
        result.first = curr[0];
        result.second = curr[1];
            
            return result ;  
        
    }
};