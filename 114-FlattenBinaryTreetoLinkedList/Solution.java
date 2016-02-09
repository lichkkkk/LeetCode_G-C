/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
 * 114. Flatten Binary Tree to Linked List
 * Tag: Recursion
 * Chang Li at UC San Diego
 * Feb. 9, 2016
 */
public class Solution {
    public void flatten(TreeNode root) {
        if (root != null) {
            helper(root);
        }
    }

    /** Return the last node of the flattened Binary Tree */
    public TreeNode helper(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root;
        } else if (root.right == null) {
            root.right = root.left;
            root.left = null;
            return helper(root.right);
        } else if (root.left == null) {
            return helper(root.right);
        } else {
            TreeNode tmp = root.right;
            root.right = root.left;
            root.left = null;
            helper(root.right).right = tmp;
            return helper(tmp);
        }
    }
}
