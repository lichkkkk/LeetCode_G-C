/*
 * Easy problem. Just check from two sides and move towards the center.
 *
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */

public class Solution {
    public boolean isStrobogrammatic(String num) {
        for(int i=0; i<(num.length()+1)/2; i++) {
            if(!isSymm(num.charAt(i), num.charAt(num.length()-i-1))) {
                return false;
            }
        }
        return true;
    }
    
    public boolean isSymm(char a, char b) {
        if(a == b) {
            if(a == '1' || a == '8' || a == '0') {
                return true;
            }else {
                return false;
            }
        }else if(a == '6' && b == '9') {
            return true;
        }else if(a == '9' && b == '6') {
            return true;
        }else {
            return false;
        }
    }
}
