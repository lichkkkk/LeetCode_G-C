/**
 * 859. Buddy String [Easy]
 * Start to do LeedCode again, since need to prepare for the DeepMind interview.
 * Jun.21 2019, 1:20 AM
 * Jersey City, NJ
 */
class Solution {
    public boolean buddyStrings(String A, String B) {
        int lenA = A.length();
        int lenB = B.length();
        if (lenA != lenB) {
            return false;
        }
        int diffCount = 0;
        int[] diffIndex = new int[2];
        boolean[] charsAppeared = new boolean[26];
        boolean hasDuplicate = false;
        for (int i=0; i<lenA; i++) {
            char charA = A.charAt(i);
            char charB = B.charAt(i);
            if (charA != charB) {
                if (diffCount >= 2) {
                    return false;
                }
                diffIndex[diffCount] = i;
                diffCount++;    
            }
            int charOrd = charA - 'a';
            hasDuplicate |= charsAppeared[charOrd];
            charsAppeared[charOrd] = true;
        }
        if (diffCount == 2) {
            return A.charAt(diffIndex[0]) == B.charAt(diffIndex[1]) &&
                A.charAt(diffIndex[1]) == B.charAt(diffIndex[0]);
        } else if (diffCount == 0) {
            return hasDuplicate;
        } else {
            return false;
        }
    }
}
