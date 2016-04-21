/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode upsideDownBinaryTree(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode[] pair= helper(root);
        return pair[1];
    }
    public TreeNode[] helper(TreeNode node) {
        if (node.left != null) {
            TreeNode[] pair= helper(node.left);
            if (node.right != null) {
                pair[0].left = new TreeNode(node.right.val);
            }
            pair[0].right = new TreeNode(node.val);
            TreeNode[] res = {pair[0].right,pair[1]};
            return res;
        }
        else {
            TreeNode[] res = {node,node};
            return res;
        }
    }
}