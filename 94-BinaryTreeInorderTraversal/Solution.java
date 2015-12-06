/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
 * The Recursion Solution is trivial. If we want to do this in a non-
 * recursion way, we need to use a stack. To know if one node has 
 * already been visited, I used another stack.
 *
 * Running Time: O(n) Time, O(h) Space
 *
 * Chang Li at UC San Diego
 * Dec. 5, 2015
 */

public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new LinkedList<Integer>();
        if(root == null) {
            return res;
        }
        LinkedList<TreeNode> stack = new LinkedList<TreeNode>();
        LinkedList<Boolean> visited = new LinkedList<Boolean>();
        stack.push(root);
        visited.push(false);
        while(!stack.isEmpty()) {
        	TreeNode node = stack.pop();
        	if(visited.pop() == true) {
        		res.add(node.val);
	        }else {
        		if(node.right != null) {
        			stack.push(node.right);
	        		visited.push(false);
	        	}
        		stack.push(node);
        		visited.push(true);
        		if(node.left != null) {
        			stack.push(node.left);
        			visited.push(false);
        		}
	        }
        }
        return res;
    }
}
