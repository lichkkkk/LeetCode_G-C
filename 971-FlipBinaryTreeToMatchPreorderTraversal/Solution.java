/**
 * 971. Flip Binary Tree To Match Preorder Traversal
 * Jun. 22, 2019 Google NYC
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
    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        List<Integer> res = new LinkedList<>();
        if (traverseAndFlip(root, voyage, 0, res) == voyage.length) {
          return res;
        } else {
          res.clear();
          res.add(-1);
          return res;
        }
    }
  
    // Return the next index of vayage that we should start to match
    // Return -1 if the current match is not doable
    private static int traverseAndFlip(
      TreeNode root, int[] voyage, int startPosition, List<Integer> res) {
        if (root == null) {
          return startPosition;
        }
        if (voyage[startPosition] != root.val) {
          return -1;
        }
        startPosition += 1;
        if (root.left == null) {
          return traverseAndFlip(root.right, voyage, startPosition, res);
        } else if (root.left.val == voyage[startPosition]) {
          startPosition = traverseAndFlip(root.left, voyage, startPosition, res);
          if (startPosition != -1) {
            return traverseAndFlip(root.right, voyage, startPosition, res);
          } else {
            return -1;
          }
        } else if (root.right != null && root.right.val == voyage[startPosition]) {
          res.add(root.val);
          startPosition = traverseAndFlip(root.right, voyage, startPosition, res);
          if (startPosition != -1) {
            return traverseAndFlip(root.left, voyage, startPosition, res);
          } else {
            return -1;
          }
        } else {
          return -1;
        }
    }
}
