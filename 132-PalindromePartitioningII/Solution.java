class Solution {
    public int minCut(String s) {
        return helper(s, 0, new HashMap<Integer, Integer>());
    }
    
    private static int helper(String s, int start, Map<Integer, Integer> cache) {
        if (cache.containsKey(start)) {
            return cache.get(start);
        }
        if (isPalindrome(s, start, s.length())) {
            return 0;
        }
        int res = s.length() - start;
        for (int end=s.length()-1; end>start; end--) {
            if (isPalindrome(s, start, end)) {
                res = Math.min(res, helper(s, end, cache) + 1);
            }
        }
        cache.put(start, res);
        return res;
    }
    
    private static boolean isPalindrome(String s, int start, int end) {
        //System.out.println(s.substring(start, end));
        for (int i=start; i*2-start < end-1; i++) {
            if (s.charAt(i) != s.charAt(end-1-i+start)) {
                return false;
            }
        }
        return true;
    }
}
