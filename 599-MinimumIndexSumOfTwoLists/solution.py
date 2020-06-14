class Solution:
    def findRestaurant2(self, list1: List[str], list2: List[str]) -> List[str]:
        scores_dict_1 = dict(zip(list1, range(len(list1))))
        curr_best_names = []
        curr_best_score = len(list1) + len(list2)
        for i in range(len(list2)):
          curr_choice = list2[i]
          if curr_choice not in scores_dict_1:
            continue
          curr_score = scores_dict_1[curr_choice] + i
          if curr_score < curr_best_score:
            curr_best_names = [curr_choice]
            curr_best_score = curr_score
          elif curr_score == curr_best_score:
            curr_best_names.append(curr_choice)
        return curr_best_names
    
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = dict(zip(list1, range(len(list1))))
        d2 = dict(zip(list2, range(len(list2))))
        common = set(list1) & set(list2)
        dc = dict([(r, d1[r] + d2[r]) for r in common])
        best = min(dc.values())
        return [r for r in common if dc[r] == best]
