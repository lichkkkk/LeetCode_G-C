/*
 * This problem is not so hard. The basic idea is scan from the left
 * to the right and record that point where the biggest height changed.
 * Actually I think we don't need to defien so many objects.
 *
 * Running Time: O(n)
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */

public class Solution {
    
    class Pair implements Comparable<Pair> {
        public int x;
        public Building y;
        public boolean add;
        
        public Pair(int x, Building y, boolean add) {
            this.x = x;
            this.y = y;
            this.add = add;
        }
        
        public int compareTo(Pair p) {
            return x - p.x;
        }
        
    }
    
    class Building implements Comparable<Building>{
        public int h;
        public Building(int h) {
            this.h = h;
        }
        public int compareTo(Building b) {
            return -(this.h - b.h);
        }
    }
    
    public List<int[]> getSkyline(int[][] buildings) {
        Pair[] actions = new Pair[buildings.length * 2];
        int pos = 0;
        for(int[] b : buildings) {
            Building bd = new Building(b[2]);
            actions[pos++] = new Pair(b[0], bd, true);
            actions[pos++] = new Pair(b[1], bd, false);
        }
        Arrays.sort(actions);
        PriorityQueue<Building> height = new PriorityQueue<Building>();
        List<int[]> res = new LinkedList<int[]>();
        int oldHeight = 0;
        pos = 0;
        while(pos < actions.length) {
            
            int newHeight;
            Pair p;
            do {
                p = actions[pos++];
                if(p.add == true) {
                    height.offer(p.y);
                }else {
                    height.remove(p.y);
                }
                newHeight = height.size()==0?0:height.peek().h;
            }while(pos < actions.length && actions[pos].x == actions[pos-1].x);
            
            if(newHeight != oldHeight) {
                int[] point = {p.x, newHeight};
                res.add(point);
                oldHeight = newHeight;
            }
        }
        return res;
    }
}
