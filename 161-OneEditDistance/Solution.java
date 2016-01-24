/**
 * 161. One Edit Distance
 * Tag: String
 *      Consider different length case
 * Chang Li at UC San Diego
 * Jan. 24, 2016
 */

public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        // s.length() == t.length()
        if(s.length() == t.length()) {
            int errorCount = 0;
            for(int i=0; i<s.length(); i++) {
                if(s.charAt(i) != t.charAt(i)) {
                    errorCount += 1;
                }
            }
            if(errorCount != 1) {
                return false;
            }else {
                return true;
            }
        // s.length() == t.length() + 1
        }else if(s.length() == t.length() + 1) {
            int i=0, j=0;
            while(j < t.length() && s.charAt(i) == t.charAt(j)) {
                i ++;
                j ++;
            }
            i ++;
            while(j < t.length() && s.charAt(i) == t.charAt(j)) {
                i ++;
                j ++;
            }
            return (j == t.length());
        // s.length() == t.length() - 1
        }else if(s.length() == t.length() - 1) {
            int i=0, j=0;
            while(i < s.length() && s.charAt(i) == t.charAt(j)) {
                i ++;
                j ++;
            }
            j ++;
            while(i < s.length() && s.charAt(i) == t.charAt(j)) {
                i ++;
                j ++;
            }
            return (j == t.length());
        // diff bigger than 1
        }else {
            return false;
        }
    }
}
