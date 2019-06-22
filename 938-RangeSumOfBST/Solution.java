/**
 * 938. Ramge Sum of BST
 * Jun. 22, Google NYC
 * 
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        if (root == null || L > R) {
            return 0;
        }
        int val = root.val;
        int res = 0;
        int sum = rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R);
        if (val >= L && val <= R) {
            sum += val;
        }
        return sum;
    }
}
