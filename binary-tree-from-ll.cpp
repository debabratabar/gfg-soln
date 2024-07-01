/*

Question Link : https://www.geeksforgeeks.org/problems/delete-node-in-doubly-linked-list/1


*/


class Solution {
  public:
TreeNode* constructTree( vector<int> &values , int i  ) {
    
    
    if (i >= values.size()) return nullptr;

    TreeNode* root = new TreeNode(values[i]);
    
    root->left = constructTree(values, (2 * i) + 1);
    root->right = constructTree(values, (2 * i) + 2);

    return root;
}

void convert(Node *head, TreeNode *&root) {
    // Your code here
    vector<int> values ;
    
    while ( head != 0 ){
        values.push_back(head->data) ;
        head= head->next  ; 
    }
    
    root = constructTree(  values , 0  ); 

}
};