/*
 * I intend to use BFS at the first time. You know, this problem looks a
 * little bit like the "Number of Islands" problem. But as we only need
 * to find the boundary, the binary search would be quicker.
 *
 * Time: BFS: O(n^2), Binary Search: O(nlogn)
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */

public class Solution {
    public int minArea(char[][] image, int x, int y) {
        int start, end;
        
        int up, down, left, right;
        
        start = -1;
        end = x;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            if(checkRow(image, mid)) {
                start = mid;
            }else {
                end = mid;
            }
        }
        up = start + 1;
        
        start = x;
        end = image.length;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            if(!checkRow(image, mid)) {
                start = mid;
            }else {
                end = mid;
            }
        }
        down = start;
        
        start = -1;
        end = y;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            if(checkCol(image, mid)) {
                start = mid;
            }else {
                end = mid;
            }
        }
        left = start + 1;
        
        start = y;
        end = image[0].length;
        while(start + 1 < end) {
            int mid = start + (end - start) / 2;
            if(!checkCol(image, mid)) {
                start = mid;
            }else {
                end = mid;
            }
        }
        right = start;
        
        return (down-up+1)*(right-left+1);
    }
    
    public boolean checkRow(char[][]image, int row) {
        for(char ch : image[row]) {
            if(ch == '1') {
                return false;
            }
        }
        return true;
    }
    
    public boolean checkCol(char[][]image, int col) {
        for(int i=0; i<image.length; i++) {
            if(image[i][col] == '1') {
                return false;
            }
        }
        return true;
    }
}
