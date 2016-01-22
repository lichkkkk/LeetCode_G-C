/**
 * 168. Excel Sheet Column Title
 * Tag: Recursion
 * Chang Li at UC San Diego
 * Jan. 22, 2016
 */

public class Solution {
    public String convertToTitle(int n) {
        if(n == 0) {
            return "";
        }else {
            return convertToTitle((n-1)/26) + (char)((n-1)%26 + 'A');
        }
    }
}
