/**
 * 1054. Distant Barcodes
 * Jun. 22, 2019 Google NYC
 */
class Solution {
  public int[] rearrangeBarcodes(int[] barcodes) {
    if (barcodes == null || barcodes.length == 0) {
      return null;
    }
    // Step-1: Count and Find the most frequent element
    int currentMaxValue = 0;
    int currentMaxKey = -1;
    Map<Integer, Integer> countMap = new HashMap<>();
    for (int num : barcodes) {
      int newCount = countMap.getOrDefault(num, 0) + 1;
      countMap.put(num, newCount);
      if (newCount > currentMaxValue) {
        currentMaxValue = newCount;
        currentMaxKey = num;
      }
    }
    // Step-2: Create a Map of List
    Map<Integer, List<Integer>> mapOfList = new HashMap<>();
    for (int i=0; i<currentMaxValue; i++) {
      List<Integer> newList = new LinkedList<>();
      newList.add(currentMaxKey);
      mapOfList.put(i, newList);
    }
    // Step-3: Make sure the input is ordered
    Arrays.sort(barcodes);
    // Step-4: Iterate and put
    int currentListIndex = 0;
    for (int n : barcodes) {
      if (n == currentMaxKey) {
        continue;
      }
      mapOfList.get(currentListIndex).add(n);
      currentListIndex = (currentListIndex + 1) % currentMaxValue; 
    }
    // Step-5: Iterate the Map of List to generate the final output
    int[] res = new int[barcodes.length];
    int index = 0;
    for (int i=0; i<currentMaxValue; i++) {
      List<Integer> list = mapOfList.get(i);
      for (int n : list) {
        res[index++] = n;
      }
    }
    return res;
  }
}
