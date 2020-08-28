class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [w for w in re.split('[ !?\',;.]', paragraph.lower()) if w and w not in banned]
        return Counter(words).most_common(1)[0][0]
