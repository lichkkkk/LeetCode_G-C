/*
 * A backtracking problem. This is not a perfect solution because it used
 * too many Objects which make it slow.
 *
 * Chang Li at UC San Diego
 * Dec. 9, 2015
 */

public class Solution {
    public List<String> generatePalindromes(String s) {
        HashSet<String> res = new HashSet<String>();
        StringBuilder tmp = new StringBuilder();
        HashMap<Character, Integer> chars = new HashMap<>();
        for(int i=0; i<s.length(); i++) {
            if(chars.containsKey(s.charAt(i))) {
                chars.put(s.charAt(i), chars.get(s.charAt(i)) + 1);
            }else {
                chars.put(s.charAt(i), 1);
            }
        }
        Set<Character> charSet = new HashSet<Character>(chars.keySet());
        for(char ch : charSet) {
            if(chars.get(ch) % 2 == 1) {
                tmp.append(ch);
                if(chars.get(ch) == 1) {
                    chars.remove(ch);
                }else {
                    chars.put(ch, chars.get(ch)-1);
                }
            }
        }
        if(tmp.length() <= 1) {
            helper(res, chars, tmp);
        }
        return new LinkedList<String>(res);
    }
    
    public void helper(HashSet<String> res, Map<Character, Integer> chars, StringBuilder tmp) {
        if(chars.keySet().size() == 0) {
            res.add(tmp.toString());
        }else {
            Set<Character> charSet = new HashSet<Character>(chars.keySet());
            for(char ch : charSet) {
                tmp.insert(0, ch);
                tmp.append(ch);
                if(chars.get(ch) == 2) {
                    chars.remove(ch);
                }else {
                    chars.put(ch, chars.get(ch)-2);
                }
                helper(res, chars, tmp);
                tmp.deleteCharAt(0);
                tmp.deleteCharAt(tmp.length()-1);
                if(chars.containsKey(ch)) {
                    chars.put(ch, chars.get(ch)-2);
                }else {
                    chars.put(ch, 2);
                }
            }
        }
    }
}
