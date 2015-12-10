/*
 * Basic problems about hashtable.
 *
 * Chang Li at UC San Diego
 * Dec. 9, 2015
 */

public class ValidWordAbbr {
    
    HashMap<String, Boolean> abbrDict = new HashMap<String, Boolean>();
    HashSet<String> dict = new HashSet<String>();
    
    public ValidWordAbbr(String[] dictionary) {
        for(String word : dictionary) {
            if(dict.contains(word)) {
                continue;
            }
            dict.add(word);
            String abbr;
            if(word.length() <= 2) {
                abbr = word + "";
            }else {
                abbr = "" + word.charAt(0) + (word.length()-2) + word.charAt(word.length()-1);
            }
            if(abbrDict.containsKey(abbr)) {
                abbrDict.put(abbr, false);
            }else {
                abbrDict.put(abbr, true);
            }
        }
    }

    public boolean isUnique(String word) {
        String abbr;
        if(word.length() <= 2) {
            abbr = word + "";
        }else {
            abbr = "" + word.charAt(0) + (word.length()-2) + word.charAt(word.length()-1);
        }
        if(abbrDict.containsKey(abbr)) {
            if(dict.contains(word)) {
                return abbrDict.get(abbr);
            }else {
                return false;
            }
        }else {
            return true;
        }
    }
}


// Your ValidWordAbbr object will be instantiated and called as such:
// ValidWordAbbr vwa = new ValidWordAbbr(dictionary);
// vwa.isUnique("Word");
// vwa.isUnique("anotherWord");
