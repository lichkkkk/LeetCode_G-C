class Solution:
    def uncommonFromSentences2(self, A: str, B: str) -> List[str]:
        appeared_once = set()
        appeared_more = set()
        for s in A.split() + B.split():
          if s in appeared_more:
            continue
          elif s in appeared_once:
            appeared_once.remove(s)
            appeared_more.add(s)
          else:
            appeared_once.add(s)
        return list(appeared_once)
    
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        counter = Counter(A.split() + B.split())
        return [k for k in counter.keys() if counter[k] == 1]
