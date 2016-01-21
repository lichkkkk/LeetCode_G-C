/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 * 
 * 297. Serialize and Deserialize Binary Tree
 * Tag: BST Traversal; BFS
 * 
 *  I used BFS in this solution, but it looks a little bit dumb.
 *  If I could use the split() method of String, the deserialize part would be more elegant.
 *  The solution with pre-order traversal and recursion looks better.
 * 
 * Chang Li at UC San Diego
 * Jan. 20, 2016
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if(root == null) return "null#";
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        StringBuilder res = new StringBuilder();
        while(queue.size() > 0) {
            TreeNode node = queue.poll();
            if(node == null) {
                res.append("null#");
            }else {
                res.append(node.val + "#");
                queue.offer(node.left);
                queue.offer(node.right);
            }
        }
        return res.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        int pos = 0;
        // Init the first node
        TreeNode root = new TreeNode(0);
        int nextPos = data.indexOf('#', pos);
        String element = data.substring(pos, nextPos);
        pos = nextPos + 1;
        if(element.equals("null")) {
            return null;
        }else {
            root.val = Integer.parseInt(element);
        }
        // Init the queue
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        // deserialize
        while(pos < data.length()) {
            // Get the next two elements
            nextPos = data.indexOf('#', pos);
            String elementLeft = data.substring(pos, nextPos);
            pos = nextPos + 1;
            // Pos will not exceed the boundary here
            nextPos = data.indexOf('#', pos);
            String elementRight = data.substring(pos, nextPos);
            pos = nextPos + 1;
            // Get the "host" node
            TreeNode node = queue.poll();
            // Parse the first element
            if(elementLeft.equals("null")) {
                node.left = null;
            }else {
                node.left = new TreeNode(Integer.parseInt(elementLeft));
                queue.offer(node.left);
            }
            // Parse the second element
            if(elementRight.equals("null")) {
                node.right = null;
            }else {
                node.right = new TreeNode(Integer.parseInt(elementRight));
                queue.offer(node.right);
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
