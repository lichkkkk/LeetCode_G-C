/**
 * 318. Maximum Product of Word Lengths
 * Tag: String, Bit Manipulation
 *      Bit Manipulation is a good idea, which I failed to figure out at first
 * Chang Li at UC San Diego
 * Jan. 22, 2016
 */

public class Solution {
    public int maxProduct(String[] words) {
        if(words == null || words.length == 0) {
            return 0;
        }
        // Build a bit-char table to memorize which chars each word contains
        int[] charTable = new int[words.length];
        for(int i=0; i<words.length; i++) {
            String str = words[i];
            for(int pos=0; pos<str.length(); pos++) {
                int mask = 1 << (str.charAt(pos) - 'a');
                charTable[i] = charTable[i] | mask;
            }
        }
        // Begin check
        int max = 0;
        for(int i=0; i<words.length-1; i++) {
            for(int j=i+1; j<words.length; j++) {
                if((charTable[i] & charTable[j]) == 0) {
                    max = Math.max(max, words[i].length() * words[j].length());
                }
            }
        }
        return max;
    }
}
