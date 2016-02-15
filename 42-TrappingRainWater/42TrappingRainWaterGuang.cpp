class Solution {
public:
    int trap(vector<int>& height) {
        
        int width = height.size();
        
        if(width <= 2) return 0;
        
        //vector<int> llevel(width, 0);
        //vector<int> rlevel(width, 0);
        
        int llevel[width] = {0};
        int rlevel[width] = {0};
        
        for(int i = 1; i < width; i++){
            int level = llevel[i-1] + height[i-1];
            
            if(level > height[i]){
                llevel[i] = level - height[i];
            }
            
        }
        
        int v = 0;
        for(int i = width - 2; i > 0; i--){
            
            int level = rlevel[i+1] + height[i+1];
            
            if(level >= height[i] + llevel[i]){
                v += llevel[i];
                rlevel[i] = llevel[i];
            }
            else if(level >= height[i]){
                rlevel[i] = level - height[i];
                v += rlevel[i];
            }
            
        }    
        
        return v;
    }
};
