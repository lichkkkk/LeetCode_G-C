/**
 * Jan. 30, 2021
 * @London
 */
class Solution {
    public List<List<String>> partition(String s) {
        return helper(s, 0, new HashMap<Integer, List<List<String>>>());
    }
    
    public List<List<String>> helper(String s, int start, Map<Integer, List<List<String>>> cache) {
        if (start == s.length()) {
            return new ArrayList<List<String>>();
        }
        if (cache.containsKey(start)) {
            return cache.get(start);
        }
        List<List<String>> res = new ArrayList<List<String>>();
        for (int end = start+1; end <= s.length(); end++) {
            String prefix = s.substring(start, end);
            if (isPalindrome(prefix)) {
                List<List<String>> subres = helper(s, end, cache);
                if (subres.isEmpty()) {
                    List<String> newEntry = new ArrayList<String>();
                    newEntry.add(prefix);
                    res.add(newEntry);
                } else {
                    for (List<String> partition : subres) {
                        List<String> copy = new ArrayList<String>(partition);
                        copy.add(0, prefix);
                        res.add(copy);
                    }
                }
            }
        }
        cache.put(start, res);
        return res;
    }
    
    private static boolean isPalindrome(String s) {
        for (int i=0; i*2 < s.length(); i++) {
            if (s.charAt(i) != s.charAt(s.length()-1-i)) {
                return false;
            }
        }
        return true;
    }
}
