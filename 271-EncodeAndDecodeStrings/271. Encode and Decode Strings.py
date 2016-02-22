__author__ = 'liuxiyun'
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for string in strs:
            res+='#'
            for letter in string:
                res+=str(ord(letter))
                res+=" "
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        #12 13 14 #15 16 #
        res = []
        i=0
        while i<len(s):
            if s[i] == '#':
                res.append("")
                i+=1
                continue
            j = i
            while s[j]!=' ':
               j+=1
            res[-1]+=chr(int(s[i:j]))
            i=j+1
        return res
class Codec2:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for string in strs:
            res=res+str(len(string))+'#'+string
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        #12 13 14 #15 16 #
        res = []
        i=0
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i = j+length+1
            # print s[j+1:j+length+1]
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
c=Codec2()
print c.encode(['Hi',',','You'])
print c.decode(c.encode(['Hi',',','You']))