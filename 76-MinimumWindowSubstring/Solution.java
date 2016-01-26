/**
 * 76. Minimum Window Substring
 * Tag: Two Pointers, Sliding Window
 *      When You feel blue, just do something meaningful and then everything will be fine!
 * Chang Li at UC San Diego
 * Jan. 25, 2016
 */
 
public class Solution {
    public String minWindow(String s, String t) {
        if(s == null || t == null || s.length() == 0 || t.length() == 0) {return "";}
        
        // Dealing with string t
        Map<Character, Integer> charMap = new HashMap<>();
        int count = 0;
        for(int i=0; i<t.length(); i++) {
            char ch = t.charAt(i);
            if(!charMap.containsKey(ch)) {
                charMap.put(ch, count);
                count++;
            }
        }
        int[] memTable = new int[count]; /* This is to record the appearance of each char in t */
        int[] countTable = new int[count];
        for(int i=0; i<t.length(); i++) {
            char ch = t.charAt(i);
            countTable[charMap.get(ch)] += 1;
        }
        
        // Find the first window from the left most
        int left = s.length();
        int right = s.length()-1;
        while(left > 0 && count > 0) {
            left -= 1;
            char ch = s.charAt(left);
            if(charMap.containsKey(ch)) {
                int ind = charMap.get(ch);
                memTable[ind] += 1;
                if(memTable[ind] == countTable[ind]) {
                    count -= 1;
                }
            }
        }
        if(count != 0) {
            return "";
        }
        
        // Okay! We have already found a valid window!
        // Now, let's slide it and shrink it to find the minimum one
        int windowLength = right - left + 1;
        int minLeft = left;
        int minRight = right;
        while(left >= 0) {
            // Shrink first
            while((!charMap.containsKey(s.charAt(right))) || 
                        memTable[charMap.get(s.charAt(right))] > countTable[charMap.get(s.charAt(right))]) {
                if(charMap.containsKey(s.charAt(right))) {
                    memTable[charMap.get(s.charAt(right))] -= 1;
                }
                right -= 1;
            }
            // Update the minimum window length
            if(right-left+1 < windowLength) {
                windowLength = right-left+1;
                minLeft = left;
                minRight = right;
            }
            // Slide the window to the left
            left -= 1;
            while(left >= 0 && !charMap.containsKey(s.charAt(left))) {
                left -= 1;
            }
            if(left >= 0) {
                memTable[charMap.get(s.charAt(left))] += 1;
            }
        }
        
        return s.substring(minLeft, minRight+1);
    }
}
