public class Solution {
    // Use stacks. Calculate the value in the parentheses when meet a right parenthese
    // Complexity: O(n) time O(n) space
    // Chang Li at UC San Diego
    // Dec. 5, 2015
    public int calculate(String s) {
        	if(s == null || s.length() == 0) {
    			return 0;
    		}
    		s = "(" + s + ")";
    		LinkedList<Integer> numStack = new LinkedList<Integer>();
    		LinkedList<Character> optrStack = new LinkedList<Character>();
    		// Use StringBuffer can make the boundary condition easier to process
    		// Another solution is when we meet one number, we read all of its digits there, but in that
    		// way you need to maintain the index i properly
    		StringBuilder numBuf = new StringBuilder();
    		// For loop is safe and simple
            for(int i=0; i<s.length(); i++) {
            	char ch = s.charAt(i);
    			if(ch == ' ') {
    				continue;
    			}else if(ch >= '0' && ch <= '9') {
    				numBuf.append(ch);
    			}else if(ch != ')'){
    				optrStack.push(ch);
    				if(numBuf.length() > 0) {
    					numStack.push(Integer.parseInt(numBuf.toString()));
    					numBuf.delete(0, numBuf.length());
				    }
			    }else if(ch == ')'){
			        if(numBuf.length() > 0) {
    					numStack.push(Integer.parseInt(numBuf.toString()));
    					numBuf.delete(0, numBuf.length());
				    }
				    // Handle expression like "(5+4-3+2"
		    		int value = 0;
		    		char optr;
		    		while((optr = optrStack.pop()) != '(') {
		    			int curNum = numStack.pop();
		    			if(optr == '-') {
		    				value -= curNum;
		    			}else {
		    				value += curNum;
		    			}
		    		}
	    			value += numStack.pop();
	    			numStack.push(value);
	    		}
		    }
		    return numStack.pop();
    }
}
