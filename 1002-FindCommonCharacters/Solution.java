/**
 * 1002. Find Common Characters
 * Jun. 25, 2019 50 Columbus
 */
class Solution {
    public List<String> commonChars(String[] A) {
        int[][] masks = new int[A.length][];
        masks[0] = getMask(A[0]);
        int[] res = masks[0];
        for (int i=1; i<A.length; i++) {
            masks[i] = getMask(A[i]);
            res = findOverlap(res, masks[i]);
        }
        LinkedList<String> resList = new LinkedList<>();
        for (int i=0; i<res.length; i++) {
            for (int count=res[i]; count>0; count--) {
                resList.add(Character.toString((char) ('a' + i)));
            }
        }
        return resList;
    }
    
    private static int[] getMask(String s) {
        int[] res = new int[26];
        for (char c : s.toCharArray()) {
            res[c-'a'] = res[c-'a'] + 1;
        }
        return res;
    }
    
    private static int[] findOverlap(int[] a, int[] b) {
        int[] res = new int[26];
        for (int i=0; i<26; i++) {
            res[i] = Math.min(a[i], b[i]);
        }
        return res;
    }
}
