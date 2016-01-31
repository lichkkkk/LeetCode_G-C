__author__ = 'liuxiyun'
#1. Use two pointers: start and end to represent a window.
# 2. Move end to find a valid window.
# 3. When a valid window is found, move start to find a smaller window.
# To check if a window is valid, we use a dic(hashmap) to store (char, count) for chars in t.
# And use counter for the number of chars of t to be found in s.
#  The key part is dic[s[end]]--;.
# We decrease count for each char in s. If it does not exist in t, the count will be negative.
# O(n)

from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = [0]*128 # map for t
        for letter in t:
            dic[ord(letter)]+=1

        count = len(t)
        begin, end = 0,0
        head, min_len = 0, len(s)+1

        while end < len(s):
            if dic[ord(s[end])] > 0: # not all of letters in t have been included in our range now
                count -= 1 # we include this letter, and the number of letters need to be included -1
            dic[ord(s[end])]-=1 # if this letter not in t, dic[this letter] = 0-->negative
            end +=1

            while count == 0:
                if (end-begin) < min_len:
                    min_len = end-begin
                    head = begin

                dic[ord(s[begin])] += 1 # if s[begin] is in t, now our window is not big enough,
                if dic[ord(s[begin])] > 0: # since dic[s[begin]] > 0, we increase the # letter need to be found
                    count += 1 # if s[begin] not in t, dic[s[begin]] is still <= 0, because it cannot be larger than 0
                begin += 1

        return s[head:min_len+head] if (min_len <= len(s)) else ""

# O(n^2) sucks T^T
from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # res = [len(s)+1 for i in range(len(s))]]

        index = [-1 for j in range(len(t))]
        # each position represent each letter in t, each value represents the index in t
        dict_index = defaultdict(list)
        # key: letter in t, value: the letter's index in t
        min_window = [-1,-1]
        # track the window
        smallest_len = len(t)+1
        for i in range(0,len(t)):
            dict_index[t[i]].append(i)
        # i is the index in s, add i(index in t) to dict, index[i] represents the index in t
        # print dict_index
        # print index
        for i in range(0,len(s)): # go through s
            if s[i] in dict_index: # if s[i] is the letter in t
                # if there are multiple same letter in t, we want to update the one with smallest index in t
                min_index = index[dict_index[s[i]][0]] # track the smallest index of letter s[i] in t
                min_index_of_index = dict_index[s[i]][0] # track the index of this letter with [smallest index in t]in index
                for ii in dict_index[s[i]]: # go through this letter's every possible index in t
                    if index[ii] < min_index: # if has smaller index in t
                        min_index_of_index = ii # update
                    # print "set min_index"
                    # min_index = min(min_index,index[dict_index[s[i]][ii]])
                # print 's[i]',i,' ',s[i],'   ','index[min_index_of_index]',index[min_index_of_index],'index:',index
                index[min_index_of_index] = i
                # print 's[i]',i,' ',s[i],'   ','index[min_index_of_index]',index[min_index_of_index],'index:',index


                # print 'max_index:',min_window[1]
                # print "min_index",min_index_index,"index ",index
                if -1 in index:
                    continue
                else:
                    upperbound = max(index)
                    lowerbound = min(index)
                    if upperbound - lowerbound +1 <smallest_len:
                        smallest_len = upperbound - lowerbound +1
                        min_window[1]=upperbound
                        min_window[0]=lowerbound
                # print 'max_index:',min_window[1],' min_index:',min_window[0]
            # else:
            #     if i!=0:
                    # res[i] = res[i-1]+1
        return s[min_window[0]:min_window[1]+1] if (-1 not in min_window) else ""
# Test case:
# # "aa", "aa"
# # 'a', 'a'
c=Solution()
# print c.minWindow("bbaa","aba")
print c.minWindow("abcdabcd","acd")