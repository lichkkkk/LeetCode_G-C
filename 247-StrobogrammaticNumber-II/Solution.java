/*
 * Classic backtracking problem. DFS. Remember to delete added data
 * after children return back.
 *
 * Time: O(5^n), Space(n)
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */

public class Solution {
    
    public char[] nums = {'0', '1', '8', '6', '9'};
    
    public List<String> findStrobogrammatic(int n) {
        List<String> res = new LinkedList<String>();
        StringBuilder tmp = new StringBuilder();
        if(n % 2 == 0) {
            helper(res, tmp, n);
        }else {
            for(int i=0; i<3; i++) {
                tmp.append(nums[i]);
                helper(res, tmp, n-1);
                tmp.deleteCharAt(0);
            }
        }
        return res;
    }
    
    public void helper(List<String> res, StringBuilder tmp, int digits) {
        if(digits == 0) {
            if(tmp.length() == 1 || tmp.charAt(0) != '0') {
                res.add(tmp.toString());
            }
        }else {
            for(char ch : nums) {
                myAppend(tmp, ch);
                helper(res, tmp, digits-2);
                tmp.deleteCharAt(0);
                tmp.deleteCharAt(tmp.length()-1);
            }
        }
    }
    
    public void myAppend(StringBuilder tmp, char ch) {
        if(ch == '0' || ch == '1' || ch == '8') {
            tmp.insert(0, ch);
            tmp.append(ch);
        }else if(ch == '6') {
            tmp.insert(0, '9');
            tmp.append(ch);
        }else if(ch == '9') {
            tmp.insert(0, '6');
            tmp.append('9');
        }
    }
    
}
