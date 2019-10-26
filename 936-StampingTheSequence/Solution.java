/**
 * 936. Stamping The Sequence
 * Jun. 23, 2019 Google NYC
 */
class Solution {
    public int[] movesToStamp(String stamp, String target) {
        if (stamp == null || target == null || target.length() < stamp.length()) {
            return new int[0];
        }
        if (stamp.isEmpty() || target.isEmpty() || stamp.charAt(0) != target.charAt(0)) {
            return new int[0];
        }
        LinkedList<Integer> path = new LinkedList<>();
        path.addLast(0);
        boolean[][] failureCache = new boolean[stamp.length() + 1][target.length()];
        if (helper(target, stamp, path, 1, 1, failureCache)) {
            return path.stream().mapToInt(i->i).toArray();
        } else {
            return new int[0];
        }
    }
    
    private static boolean helper(
            String target,
            String stamp,
            LinkedList<Integer> path,
            int targetPosition,
            int stampPosition,
            boolean[][] failureCache
    ) {
        if (targetPosition == target.length()) {
            // Check no overflow
            return stampPosition == stamp.length();
        }
        // 0. Check failure cache
        if (failureCache[stampPosition][targetPosition]) {
            return false;
        }
        // 1. Try to start a new stamp
        if (stamp.charAt(0) == target.charAt(targetPosition)) {
            path.addLast(targetPosition);
            if (helper(target, stamp, path, targetPosition+1, 1, failureCache)) {
                return true;
            } else {
                path.removeLast();
            }
        }
        // 2. Try to use the previsous stamp
        if (stampPosition < stamp.length() &&
            stamp.charAt(stampPosition) == target.charAt(targetPosition)) {
            if (helper(target, stamp, path, targetPosition+1, stampPosition+1, failureCache)) {
                return true;
            }
        }
        // 3. If this is the end of previous stamp, we cab start from any position
        if (stampPosition == stamp.length()) {
            // Any position is possible since this is the end of previsou stamp
            for (int newStampPosition=1; newStampPosition<stamp.length(); newStampPosition++) {
                if (stamp.charAt(newStampPosition) == target.charAt(targetPosition)) {
                    path.addFirst(targetPosition-newStampPosition);
                    if (helper(target, stamp, path,
                               targetPosition+1, newStampPosition+1, failureCache)) {
                        return true;
                    } else {
                        path.removeFirst();
                    }
                }
            }
        }
        // 4. Update cache and return
        failureCache[stampPosition][targetPosition] = true;
        return false;
    }
}
