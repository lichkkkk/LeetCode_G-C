/*
 * Directly implemented with some flags and pointers.
 * Quicker but longer.
 *
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */

public class ZigzagIterator {

    public List<Integer> v1;
    public List<Integer> v2;
    public List<Integer> curList;
    public int curPos = 0;
    public boolean atFirstList = true;
    public boolean oneListEmpty = false;
    public boolean twoListEmpty = false;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        this.v1 = v1;
        this.v2 = v2;
        int l1 = v1.size();
        int l2 = v2.size();
        if(l1 == 0 && l2 == 0) {
            twoListEmpty = true;
        }else if(l1 == 0) {
            oneListEmpty = true;
            curList = v2;
        }else if(l2 == 0) {
            oneListEmpty = true;
            curList = v1;
        }else {
            curList = v1;
        }
    }

    public int next() {
        if(twoListEmpty) {
            return -1;
        }
        int next = curList.get(curPos);
        if(oneListEmpty) {
            if(curPos == curList.size()-1) {
                twoListEmpty = true;
            }else {
                curPos ++;
            }
        }else {
            if(curPos == curList.size()-1) {
                oneListEmpty = true;
            }
            if(atFirstList) {
                atFirstList = false;
                curList = v2;
            }else {
                atFirstList = true;
                curList = v1;
                curPos++;
            }
        }
        return next;
    }

    public boolean hasNext() {
        return !twoListEmpty;
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */
