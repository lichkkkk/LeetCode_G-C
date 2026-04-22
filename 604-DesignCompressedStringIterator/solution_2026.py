class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.ptr = 0
        self.char = None
    
    def _loadNextChar(self) -> None:
        if self.ptr == len(self.s):
            return
        ch = self.s[self.ptr]
        cnt = 1
        self.ptr += 1
        if self.ptr < len(self.s) and self.s[self.ptr].isdigit():
            digit_start = self.ptr
            while self.ptr < len(self.s) and self.s[self.ptr].isdigit():
                self.ptr += 1
            cnt = int(self.s[digit_start:self.ptr])
        self.char = [ch, cnt]

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        res = self.char[0]
        self.char[1] -= 1
        if not self.char[1]:
            self.char = None
        return res
        
    def hasNext(self) -> bool:
        if self.char:
            return True
        if self.ptr == len(self.s):
            return False
        self._loadNextChar()
        return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
