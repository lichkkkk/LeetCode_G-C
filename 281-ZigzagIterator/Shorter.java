/*
 * Implemented with java Iterator Object.
 * The core logic is "if another has Next, switch to another"
 * This is a little bit slower than another version.
 *
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */


public class ZigzagIterator {
    
    public Iterator<Integer> i, j, tmp;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        i = v2.iterator();
        j = v1.iterator();
    }

    public int next() {
        if(j.hasNext()) {
            tmp = i;
            i = j;
            j = tmp;
        }
        return i.next();
    }

    public boolean hasNext() {
        return i.hasNext() || j.hasNext();
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */
