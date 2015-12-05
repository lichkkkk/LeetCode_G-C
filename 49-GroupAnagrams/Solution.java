/*
 * The core issue of this problem is how to judge if two word are 
 * in the same class and if there already exists such a class.
 * The second one can be solved with HashMap. To solve the first one,
 * sort the string and then we can judge.
 * One trick is that we need to sort the strs array at the very beginning
 * to make sure the inner list of the result is in order.
 *
 * Chang Li at UC San Diego
 * Dec. 4, 2015
 */

public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new LinkedList<List<String>>();
        if(strs == null) {
            return res;
        }
        // This sort to make sure the output inner list is ordered
        Arrays.sort(strs);
        HashMap<String, List> map = new HashMap<String, List>();
        // O(n) loop
        for(String str : strs) {
	        char[] array = str.toCharArray();
	        Arrays.sort(array);
	        String sorted = new String(array);
	        // If this pattern hasn't appeared before
	        if(!map.containsKey(sorted)) {
		        List lst = new LinkedList<String>();
		        map.put(sorted, lst);
		        res.add(lst);
	        }
    	    map.get(sorted).add(str);
        }
        return res;
    }
}
