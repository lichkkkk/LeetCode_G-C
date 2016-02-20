/**
 * 320. Generalized Abbreviation
 * Tag: String, Recursion, DFS
 * 
 *      Basically, there are two kinds of ways to solve this problem.
 *      - By recursion, you can get the solution by combine the sub-solution of 
 *                      'word length - 1' input and the last chararcter;
                        (Like BFS)
 *      - By DFS, you just traverse all possible combinations.
 *      Generally speaking, the DFS should be faster, as the operation of string 
 *      in the resursion way is really slow.
 * 
 * Chang Li at UC San Diego
 * Feb. 20, 2016
 */

public class Solution {
    public List<String> generateAbbreviations(String word) {
        List<String> res = new LinkedList<String>();
        if (word == null) return res;
        
        StringBuilder stringBuilder = new StringBuilder();
        int currPos = 0;
        // DFS via Recursion
        helper(res, word, stringBuilder, currPos);
        return res;
    }
    
    public void helper(List<String> res, String word, StringBuilder currAbbr, int currPos) {
        if (currPos >= word.length()) {
            res.add(currAbbr.toString());
            return;
        }
        
        // Don't abbreviate here
        currAbbr.append(word.charAt(currPos));
        helper(res, word, currAbbr, currPos+1);
        currAbbr.deleteCharAt(currAbbr.length()-1);
        
        // Abbreviate but not till the end
        for (int i=1; i<word.length()-currPos; i++) {
            // A subtle bug: i may have two digits, so we need to know its exact length
            String toAppend = i + "" + word.charAt(currPos+i);
            currAbbr.append(toAppend);
            helper(res, word, currAbbr, currPos+i+1);
            currAbbr.delete(currAbbr.length()-toAppend.length(), currAbbr.length());
        }
        
        // Abbreviate all the rest
        res.add(currAbbr.toString() + (word.length()-currPos));
    }
}
