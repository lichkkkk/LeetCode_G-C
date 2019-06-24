/**
 * 1028. Recover a Tree From Preorder Traversal
 * Jun. 23, 2019 Google NYC
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
    public TreeNode recoverFromPreorder(String S) {
        TreeNode dummy = new TreeNode(-1);
        addNode(dummy, processString(S), 0);
        return dummy.left;
    }
    
    private static void addNode(TreeNode root, Queue<List<Integer>> queue, int depth) {
        if (queue.isEmpty()) {
            return;
        }
        // Try to add to left
        List<Integer> nextLeft = queue.peek();
        int nextLeftDepth = nextLeft.get(0);
        int nextLeftNode = nextLeft.get(1);
        if (nextLeftDepth != depth) {
            return;
        }
        root.left = new TreeNode(nextLeftNode);
        queue.poll();
        addNode(root.left, queue, depth+1);
        // Try to add to right
        if (queue.isEmpty()) {
            return;
        }
        List<Integer> nextRight = queue.peek();
        int nextRightDepth = nextRight.get(0);
        int nextRightNode = nextRight.get(1);
        if (nextRightDepth != depth) {
            return;
        }
        root.right = new TreeNode(nextRightNode);
        queue.poll();
        addNode(root.right, queue, depth+1);
    }
    
    private static Queue<List<Integer>> processString(String S) {
        int pos = 0;
        Queue<List<Integer>> queue = new LinkedList<>();
        while (pos < S.length()) {
            int depth = 0;
            while (pos < S.length() && S.charAt(pos) == '-') {
                depth++;
                pos++;
            }
            int node = 0;
            while (pos < S.length() && S.charAt(pos) != '-') {
                node = node * 10 + S.charAt(pos) - '0';
                pos++;
            }
            List<Integer> list = new LinkedList<>();
            list.add(depth);
            list.add(node);
            queue.offer(list);
        }
        return queue;
    }
}
