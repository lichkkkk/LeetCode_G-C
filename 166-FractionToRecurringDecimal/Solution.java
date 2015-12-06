// Core of this problem if to use HashMap to detect the reapeating part
// What's more, it's also crucial to figure out the while loop, which is the basic computing structure
// Cirner case include negative input numer, only Integer part and overflow when change negative number to positive one
// The easiest way to avoid overflow issue is to use Long
// Chang Li at UC San Diego
// Dec. 5, 2015

public class Solution {
    public String fractionToDecimal(int n, int d) {
        // In cae of Overflow
		long numerator = (long)n;
		long denominator = (long)d;
		if(denominator == 0 || numerator == 0) return "0";
		// Handle the negative input
        StringBuilder res = new StringBuilder();
		if(numerator > 0 && denominator < 0) {
            res.append('-');
            denominator *= -1;
        }else if(numerator < 0 && denominator > 0) {
            res.append('-');
            numerator *= -1;
        }else if(numerator < 0 && denominator < 0) {
            numerator *= -1;
            denominator *= -1;
        }
        // Append the part before the radix point
        res.append(numerator/denominator);
        numerator = numerator % denominator;
    	if(numerator > 0) {
    	   	res.append('.');
    	}else {
    	   	return res.toString();
    	}
    	// Use HashMap to find if repeating part exist
		Map<Long, Integer> visited = new HashMap<Long, Integer>();
		while(!visited.containsKey(numerator) && numerator != 0) {
			visited.put(numerator, res.length());
			numerator = numerator * 10;
			res.append(numerator/denominator);
			numerator = numerator % denominator;
		}
		// exist repeating part
		if(numerator != 0) {
			res.insert(visited.get(numerator).intValue(), '(');
			res.append(')');
		}
		return res.toString();
    }
}

