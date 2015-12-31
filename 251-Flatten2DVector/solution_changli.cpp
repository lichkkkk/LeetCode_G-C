/**
 * Chang Li
 * Dec. 31, 2015
 */

class Vector2D {
public:

    int vec_num;
    int vec_pos;
    int vec_num_max;
    vector<vector<int>>& vec2d;

    Vector2D(vector<vector<int>>& vec_2d) : vec2d(vec_2d) {
        vec_num = 0;
        vec_pos = 0;
        vec_num_max = vec2d.size()-1;
        while(vec_num_max >= 0 && vec2d[vec_num_max].size() == 0) vec_num_max --;
        while(vec_num <= vec_num_max && vec2d[vec_num].size() == 0) vec_num ++;
    }

    int next() {
        if(!hasNext()) return -1;
        int next = vec2d[vec_num][vec_pos];
        if(vec_pos + 1 < vec2d[vec_num].size()) {
            vec_pos ++;
        }else if(vec_num < vec_num_max) {
            vec_num ++;
            while(vec2d[vec_num].size() == 0) vec_num ++;
            vec_pos = 0;
        }else {
            // Reach the end
            vec_pos ++;
        }
        return next;
    }

    bool hasNext() {
        return vec_num < vec_num_max || (vec_num == vec_num_max && vec_pos < vec2d[vec_num_max].size());
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */
