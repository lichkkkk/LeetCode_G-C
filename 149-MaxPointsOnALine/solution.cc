/**
 * 149. Max Points on a Line
 *  Copied from the discuss. Too tired to write my own.
 * Chang Li @ Sunnyvale
 * Aug. 3, 2016
 * 
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point>& points) 
    {
        if(points.size()<=2) return points.size();
        int res=0;
        for(int i=0;i<points.size()-1;i++) {
            int numVertical=1,local=1,duplicate=0;
            unordered_map<double,int> map;
            for(int j=i+1;j<points.size();j++) 
                if(points[i].x==points[j].x) // special cases
                    if(points[i].y==points[j].y) // duplicate 
                        duplicate++;
                    else // vertical
                        numVertical++;
                else {
                    double slope=(points[i].y-points[j].y)*1.0/(points[i].x-points[j].x);
                    map[slope]==0?map[slope]=2:map[slope]++;
                    local=max(local,map[slope]);
                }
            local=max(local+duplicate,numVertical+duplicate);
            res=max(res,local);
        }
        return res;
    }
};
