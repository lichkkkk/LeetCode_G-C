/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 *
 * I performed awful in Google interview today. One question is to find 
 * typo in words, another is build a sharedPageMonitor Class.
 *
 * Chang Li at UC San Diego
 * Dec. 11, 2015
 */
public class Solution {
    public void connect(TreeLinkNode root) {
    		helper(root, null, null);
    }

	public void helper(TreeLinkNode root, TreeLinkNode left, TreeLinkNode right) {
		if(root == null) {
			return;
		}
		// current Layer
        if(left != null) {
			left.next = root;
			helper(root.left, left.right, root.right);
		}else {
			helper(root.left, null, root.right);
		}
		root.next = right;
		if(root.next != null) {
			helper(root.right, root.left, root.next.left);
		}else {
			helper(root.right, root.left, null);
        }
    }
}
