/*
 * Can be solved by one unit buffer.
 * Peek, next, hasNext are all O(1) operation.
 *
 * Chang Li at UC San Diego
 * Dec. 7, 2015
 */



// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    
    private boolean peekBufferEmpty = true;
    private Integer bufferedInteger;
    private Iterator<Integer> iterator;

	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    this.iterator = iterator;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        if(peekBufferEmpty) {
            if(iterator.hasNext()) {
                bufferedInteger = iterator.next();
                peekBufferEmpty = false;
            }else {
                return null;
            }
        }
        return bufferedInteger;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    Integer res = peek();
	    peekBufferEmpty = true;
	    return res;
	}

	@Override
	public boolean hasNext() {
	    return (!peekBufferEmpty) || iterator.hasNext();
	}
}
