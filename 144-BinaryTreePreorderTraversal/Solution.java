/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 * 
 * 144. Binary Tree Preorder Traversal
 * Tag: BST, Stack
 * Chang Li at UC San Diego
 * Jan. 23, 2016
 */
 
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        
        List<Integer> res = new LinkedList<>();
        if(root == null) {
            return res;
        }
        
        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.push(root);
        while(!stack.isEmpty()) {
            TreeNode node = stack.poll();
            res.add(node.val);
            if(node.right != null) {
                stack.push(node.right);
            }
            if(node.left != null) {
                stack.push(node.left);
            }
        }
        return res;
    }
}
