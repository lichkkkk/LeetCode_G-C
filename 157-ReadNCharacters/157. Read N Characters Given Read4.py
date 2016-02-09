__author__ = 'liuxiyun'
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        start = 0
        read_byte = 0
        while True:
            buffer = [""]*4
            l = read4(buffer)
            if l==4:
                buf[start:start+4] = buffer
                start+=4
                n-=4
            else:
                length = min(n,l)
                buf[start:start+length] = buffer[:length]
                break
        return start+length