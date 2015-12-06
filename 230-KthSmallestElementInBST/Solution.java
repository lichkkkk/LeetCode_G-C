/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 *
 * Because we cannot know the which branch has how many children, so 
 * we must do traversal/DFS.
 *
 * About the follow up question, we can add an attribute to each node
 * which represent how many child this node have. The the question 
 * becomes a binary search problem and the complexity is O(log(h))
 *
 * Chang Li at UC San Diego
 *
 * Dec. 5, 2015
 *
 */
public class Solution {
    
    public int count;
    public int res;
    
    public int kthSmallest(TreeNode root, int k) {
        this.count = k;
        helper(root);
        return this.res;
    }
    
    public void helper(TreeNode root) {
        if(root == null) {
            return;
        }
        // Keep diving
        helper(root.left);
        // Ok, let's go back
        count --;
        if(count == 0) {
            this.res = root.val;
            return;
        }
        // Move to another branch
        helper(root.right);
    }
}
