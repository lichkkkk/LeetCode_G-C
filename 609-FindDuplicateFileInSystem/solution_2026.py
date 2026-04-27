import os

class Solution:

    def parse(self, path: str) -> Iterable[tuple[str, str]]:
        pieces = path.split()
        path = pieces[0]
        for p in pieces[1:]:
            name, content = p.split('(')
            content = content[:-1]
            yield os.path.join(path, name), content
        
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        c2p = {}
        for p_str in paths:
            for p, c in self.parse(p_str):
                if c not in c2p:
                    c2p[c] = []
                c2p[c].append(p)
        return [v for k, v in c2p.items() if len(v) > 1]
