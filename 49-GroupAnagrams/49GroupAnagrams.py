__author__ = 'liuxiyun'
#First sort the list
#Second, we create one result list and one dictionary to save the existing hashmap and the position it should be in the result list
#Third, we do a interative loop. In the loop, for each word in the given list, we get their hashmap,
# then check if there already exist another word whose hashmap is same as this one.
# If not, we put this hashmap as key into dictionary with the index as its value
# If so, we put the word into the result list, and the position is based on the value we get from the dictionary
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        word_map = {} # key: hashmap, val:index in res
        strs.sort() # first, sort the list of strings
        for string in strs:
            this_map = [0] * 26 # create hashmap for the current word
            for letter in string:
                this_map[ord(letter)-97]+=1
            if tuple(this_map) not in word_map: # if not exist in word_map
                res.append([]) # new string.
                res[-1].append(string)
                word_map[tuple(this_map)]=len(res)-1
            else:
                res[word_map[tuple(this_map)]].append(string) # get the index and add to res[?]
        return res
# test case:
# [""]
# one word
# many word, many group

