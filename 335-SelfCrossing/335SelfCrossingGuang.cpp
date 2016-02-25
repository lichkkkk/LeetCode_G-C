class Solution {
public:
    const int para_x = 0;
    const int para_y = 1;
    struct Point{
        int x, y;
        Point(int _x, int _y) : x(_x), y(_y) {}
    };
    struct Line{
        Point p, q;
        Line(Point _p, Point _q) : p(_p), q(_q){};
    };
    bool isSelfCrossing(vector<int>& x) {
        list<Line> lines;
        Point pre(0, 0);
        int dir = 0;
        for(int i = 0; i < x.size(); i++){
            if(x[i] == 0) continue;
            Point next = pre;
            switch(dir){
                case 0:
                    next.y += x[i];
                    break;
                case 1:
                    next.x -= x[i];
                    break;
                case 2:
                    next.y -= x[i];
                    break;
                case 3:
                    next.x += x[i];
                    break;
                default:
                    break;    
            }
            dir = (dir+1)%4;
            Line current(pre, next);
            pre = next;
            //printf("line: %d, %d     %d, %d\n", current.p.x, current.p.y, current.q.x, current.q.y);            
            lines.push_back(current);
            if(lines.size() <= 3)
                continue;
                
            int cnt = 1;
            for(auto it = lines.begin(); cnt <= 3; ++it, ++cnt){
                if(lines.size() == 4 && cnt == 3) continue;
                if(intersect(current, *it))
                    return true;
            }


            // auto it = lines.begin();
            // Line before1 = *it;
            // ++it;
            // Line before2 = *it;
                        
            // if(intersect(current, before1) || intersect(current, before2)){
            //     //printf("line:interct %d, %d     %d, %d\n", current.p.x, current.p.y, current.q.x, current.q.y);
            //     return true; }
            if(lines.size() == 6)lines.pop_front();
        }
        return false;
    }
    int kind(const Line & line) {
        if(line.p.y == line.q.y)
            return para_x;
        else return para_y;    
    }
    bool pInL(Point p, Line l){
        if(kind(l) == para_x){
            if(p.y == l.p.y && p.x >= min(l.p.x, l.q.x) && p.x <= max(l.p.x, l.q.x))
                return true;
        }
        if(kind(l) == para_y){
            if(p.x == l.p.x && p.y >= min(l.p.y, l.q.y) && p.y <= max(l.p.y, l.q.y))
                return true;
        }
        return false;
    }
    bool intersect(Line l, Line m){
        Line  xLine = l;
        Line  yLine = m;
        if(kind(l) == para_x){
            if(kind(m) == para_y){
                xLine = l;
                yLine = m;
            }else{
                // l is x parallel  m is x parallel
                if(l.p.y == m.p.y && (pInL(l.p, m) ||pInL(l.q, m) ||pInL(m.p, l)||pInL(m.q, l) ))
                    return true;
                else return false;
            }
        }else{
            // l == y
            if(kind(m) == para_y){
                if(l.p.x == m.p.x && (pInL(l.p, m) ||pInL(l.q, m) ||pInL(m.p, l)||pInL(m.q, l) ))
                    return true;
                else return false;
            }
            else {
                xLine = m;
                yLine = l;
            }
        }
        int xRangeL = min(xLine.p.x, xLine.q.x);
        int xRangeR = max(xLine.p.x, xLine.q.x);
        int xRangeY = xLine.p.y;
        int yRangeX = yLine.p.x;
        int yRangeL = min(yLine.p.y, yLine.q.y);
        int yRangeH = max(yLine.p.y, yLine.q.y);
        
        if(yRangeX >= xRangeL && yRangeX <= xRangeR && xRangeY >= yRangeL && xRangeY <= yRangeH){
            //print(l);
            //print(m);
            return true;
            
        }
        return false;
    }
    void print(Line current){
        printf("weired line: %d, %d    %d, %d\n", current.p.x, current.p.y, current.q.x, current.q.y);
    }
};