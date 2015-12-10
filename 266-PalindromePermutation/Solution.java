/*
 * A simple HashTable like problem.
 *
 * Chang Li at UC San Diego
 * Dec. 9, 2015
 */

public class Solution {
    public boolean canPermutePalindrome(String s) {
        if(s == null || s.length() == 0) {
            return true;
        }
        int[] table = new int[128];
        for(int i=0; i<s.length(); i++) {
            table[s.charAt(i)] += 1;
        }
        int oddCount = 0;
        for(int n : table) {
            if(n % 2 == 1) {
                oddCount ++;
            }
        }
        if(oddCount > 1) {
            return false;
        }else {
            return true;
        }
    }
}
