/**
 * 347. Top K Frequent Elements
 * 
 * Chang Li @ Mountain view
 * Jul. 11, 2016
 */
public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int n : nums) {
            countMap.put(n, countMap.containsKey(n) ? countMap.get(n)+1 : 1);
        }
        
        List<Integer>[] buckets = new List[nums.length+1];
        for (int n : countMap.keySet()) {
            int count = countMap.get(n);
            if (buckets[count] == null) {
                buckets[count] = new ArrayList<Integer>();
            }
            buckets[count].add(n);
        }
        
        List<Integer> res = new ArrayList<>(k);
        for (int i=buckets.length-1; i>=0 && res.size()<k; --i) {
            if (buckets[i] != null) {
                for (int j=0; j<buckets[i].size() && res.size()<k; ++j) {
                    res.add(buckets[i].get(j));
                }
            }
        }
        
        return res;
    }
}
