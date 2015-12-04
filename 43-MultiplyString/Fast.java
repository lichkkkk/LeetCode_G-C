public class Fast {
    
	/*
	 * A faster implementation of string multiplication. Store the result
	 * in one array and then combine them into the result. Very clever.
	 *
	 * Chang Li Dec. 4, 2015 at UC San Diego
	 */
	
	public String multiply(String num1, String num2) {
        if(num1 == null || num2 == null) {
            return "0";
        }
        int[] product = new int[num1.length() + num2.length()];
        for(int i=0; i<num1.length(); i++) {
            for(int j=0; j<num2.length(); j++) {
                product[i+j] += (num1.charAt(num1.length()-i-1)-'0')*(num2.charAt(num2.length()-j-1)-'0');
            }
        }
        int carry =0;
        for(int i=0; i<num1.length()+num2.length(); i++) {
            int tmp = product[i] + carry;
            product[i] = tmp % 10;
            carry = tmp / 10;
        }
        StringBuilder res = new StringBuilder();
        for(int i=0; i<num1.length()+num2.length(); i++) {
            res.append(product[i]);
        }
        res = res.reverse();
        while(res.charAt(0) == '0' && res.length() > 1) {
            res.deleteCharAt(0);
        }
        return res.toString();
    }
}
