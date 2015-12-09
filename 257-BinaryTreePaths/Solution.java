/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
 * An easy backtracking/DFS problem.
 * Time: O(n), Space: O(h)
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */
public class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
    	List<String> res = new LinkedList<String>();
        if(root == null) {
        	return res;
        }
        StringBuilder path = new StringBuilder();
        helper(res, path, root);
        return res;
    }

	public void helper(List<String> res, StringBuilder path, TreeNode root){
		if(root.left == null && root.right == null) {
			res.add(path.toString() + root.val);
			return;
		}
		String curNodeStr = root.val + "->";
		path.append(curNodeStr);
		if(root.left != null) {
			helper(res, path, root.left);
		}
		if(root.right != null) {
			helper(res, path, root.right);
		}
		path.delete(path.length()-curNodeStr.length(), path.length());
	}
}
