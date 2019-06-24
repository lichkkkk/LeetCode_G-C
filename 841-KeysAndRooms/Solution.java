/**
 * 841. Keys and Rooms
 * Jun. 23, 2019 Google NYC
 */
class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        Set<Integer> visited = new HashSet<>();
        DFS(rooms, visited, 0);
        return visited.size() == rooms.size();
    }
    
    private static void DFS(List<List<Integer>> rooms, Set<Integer> visited, int roomToVisit) {
        if (visited.contains(roomToVisit)) {
            return;
        }
        visited.add(roomToVisit);
        List<Integer> keys = rooms.get(roomToVisit);
        for (int key : keys) {
            DFS(rooms, visited, key);
        }
    }
}
