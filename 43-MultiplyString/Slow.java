public class Slow {
	/*
	 * A naive implementation of String multiplication. Utilized two
	 * function: multiply-Char and add. The complexity of thie problem
	 * if O(n^2) if you don't use divide and conquer. 
	 *
	 * This implementation is slow because there are too many function
	 * calla and their parameters are all String object.
	 *
	 * Chang Li Dec. 4, 2015 at UC San Diego
	 */
	
	public String multiply(String num1, String num2) {
    	String res = "";
        if(num1 == null || num2 == null) {
		    return "0";
	    }
	    for(int i=0; i<num1.length(); i++) {
		    String temp = multiplyChar(num2, num1.charAt(i), num1.length()-i-1);
		    res = add(res, temp);
	    }
	    if(res.charAt(0) =='0') {
	        return "0";
	    }
	    return res;
    }

    public String multiplyChar(String num, char ch, int power) {
        StringBuilder res = new StringBuilder();
	    int carry = 0;
	    for(int i=0; i < num.length(); i++) {
	        int n1 = num.charAt(num.length()-i-1)-'0';
	        int n2 = ch -'0';
	        int product = n1 * n2 + carry;
		    res.append(product%10);
		    carry = product/10;
	    }
	    if(carry > 0) {
	        res.append(carry);
	    }
	    res =res.reverse();
	    if(res.charAt(0) != '0') {
		    while(power-- > 0) res.append(0);
	    }
	    return res.toString();
    }

    public String add(String num1, String num2) {
    	StringBuilder res = new StringBuilder();
	    int carry = 0;
	    for(int i=0; i < Math.max(num1.length(), num2.length()); i++) {
		    int n1 = (i<num1.length())?num1.charAt(num1.length()-i-1)-'0':0;
    		int n2 = (i<num2.length())?num2.charAt(num2.length()-i-1)-'0':0;
    		int sum = n1 + n2 + carry;
    		res.append(sum%10);
    		carry = sum/10;
    	}
    	if(carry > 0) {
    		res.append(carry);
    	}
    	return res.reverse().toString();
    }
}
