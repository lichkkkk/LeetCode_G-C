/*
 * Single Dot means current dictionary, Double means go to its parent.
 * Use a Linked List to model the path will make the process much easier.
 *
 * Corner case: [1]. the root; [2] redundent slash;
 * Running Time: O(n)
 *
 * Chang Li at UC San Diego
 * Dec. 4, 2015
 */

public class Solution {
    public String simplifyPath(String path) {
        if(path == null || path.length() == 0) {
            return "";
        }
        List<String> pathList = new LinkedList<String>();
        int pos = 1;
        while(pos < path.length()) {
	        int start = pos;
	        while(pos < path.length() && path.charAt(pos) != '/') {
		        pos++;
	        }
	        String curPath = path.substring(start, pos);
	        if(curPath.equals("..")) {
	            if(pathList.size() > 0) {
			        pathList.remove(pathList.size()-1);
	            }
		    }else if(curPath.length() > 0 && !curPath.equals(".")){
		        pathList.add(curPath);
            }
            pos++;
        }
        StringBuilder res = new StringBuilder();
        res.append('/');
        for(String p : pathList) {
	        res.append(p);
	        res.append('/');
        }
        if(res.length() > 1) {
        	res.deleteCharAt(res.length()-1);
        }
        return res.toString();
    }
}
