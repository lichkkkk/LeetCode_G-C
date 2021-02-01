/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int countNodes(TreeNode root) {
        int h = 0;
        TreeNode n = root;
        while (n != null) {
            h += 1;
            n = n.right;
        }
        int left = (int) Math.pow(2, h) - 1;
        int right = (int) Math.pow(2, h + 1) - 1;
        while (left + 1 < right) {
            // System.out.println(left + " " + right);
            int mid = left + (right - left) / 2;
            if (nodeExist(root, mid)) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return left;
    }
    
    private static boolean nodeExist(TreeNode root, int index) {
        // true -> left node; false -> right node
        List<Boolean> move = new ArrayList<>();
        while (index > 1) {
            move.add(index % 2 == 0);
            index >>= 1;
        }
        int i = move.size() - 1;
        while (i >= 0 && root != null) {
            root = move.get(i) ? root.left : root.right;
            i -= 1;
        }
        return root != null;
    }
}
