class Solution {
public:
    int minDistance(string word1, string word2) {
        
        int len1 = word1.size();
        int len2 = word2.size();
        
        if(len1 == 0) return len2;
        if(len2 == 0) return len1;
        
         vector<vector<int>> d(len1+1, vector<int>(len2+1, 0));
         d[0][0] = 0;
         
         for(int i = 1; i <= len1 ; ++i) 
            d[i][0] = i;
         for(int j = 1; j <= len2 ; ++j) 
            d[0][j] = j;
         
         
         for(int k = 2 ; k <= len1 + len2; ++k){
             for(int i = 1; i < k && i <=len1; ++i){
                 int j = k - i;
                 if(j <= len2){
                     int d1 =  min(d[i-1][j] + 1, d[i][j-1]+1);
                     int d2;
                     if(word1[i-1] == word2[j-1]) d2 =  d[i-1][j-1];
                     else d2 = d[i-1][j-1] + 1;
                     d[i][j] = min(d1, d2);
                 }
             }
         }   

        return d[len1][len2];
    }
};
