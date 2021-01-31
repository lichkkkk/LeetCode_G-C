// Tried 34 times in total to get AC
class Solution {

    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        Set<String> words = new HashSet<String>(wordList);
        if (!words.contains(endWord)) {
            return new ArrayList<List<String>>();
        }
        words.remove(beginWord);
        // Construct a graph with BFS
        Map<String, List<String>> graph = new HashMap<>();
        Queue<String> queue = new LinkedList<String>();
        queue.add(beginWord);
        while (!words.isEmpty() && !queue.isEmpty()) {
            // for (String s : queue) {
            //     System.out.print(s + " ");
            // }
            // System.out.println();
            Set<String> usedWordsThisTurn = new HashSet<String>();
            int queueSize = queue.size();
            for (int i=0; i<queueSize; i++) {
                String currWord = queue.poll();
                if (!graph.containsKey(currWord)) {
                    graph.put(currWord, new ArrayList<String>());
                } 
                List<String> nextWords = getNextWords(words, currWord);
                if (nextWords.isEmpty()) {
                    continue;
                }       
                graph.get(currWord).addAll(nextWords);
                usedWordsThisTurn.addAll(nextWords);
            }
            if (usedWordsThisTurn.isEmpty() || usedWordsThisTurn.contains(endWord)) {
                break;
            }
            words.removeAll(usedWordsThisTurn);
            for (String usedWord : usedWordsThisTurn) {
                queue.offer(usedWord);
            }
        }
        // for (String k : graph.keySet()) {
        //     System.out.print(k + ": ");
        //     for (String v : graph.get(k)) {
        //         System.out.print(v + " ");
        //     }
        //     System.out.println();
        // }
        // Find all paths in the graph with DFS
        List<List<String>> res = new ArrayList<List<String>>();
        List<String> stack = new LinkedList<String>();
        stack.add(beginWord);
        findAllPaths(graph, stack, endWord, res);
        return res;
    }
    
    private static void findAllPaths(
            Map<String, List<String>> graph, List<String> stack, String endWord, List<List<String>> res) {
        String currWord = stack.get(stack.size() - 1);
        if (currWord.equals(endWord)) {
            res.add(new ArrayList<String>(stack));
            return;
        }
        if (!graph.containsKey(currWord)) {
            return;
        }
        List<String> nextWords = graph.get(currWord);
        for (String nextWord : nextWords) {
            stack.add(nextWord);
            findAllPaths(graph, stack, endWord, res);
            stack.remove(stack.size() - 1);
        }
    }
    
    private static List<String> getNextWords(Set<String> words, String currWord) {
        List<String> res = new ArrayList<String>();
        for (String word : words) {
            if (canTransformTo(currWord, word)) {
                res.add(word);
            }
        }
        return res;
    }
    
    private static boolean canTransformTo(String begin, String end) {
        boolean hasDiff = false;
        for (int i=0; i<begin.length(); i++) {
            if (begin.charAt(i) != end.charAt(i)) {
                if (hasDiff) {
                    return false;
                } else {
                    hasDiff = true;
                }
            }
        }
        return true;
    }
}
