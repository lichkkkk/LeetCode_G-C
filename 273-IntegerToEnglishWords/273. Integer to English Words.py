__author__ = 'liuxiyun'

# Group the number by thousands (3 digits)
# dealing each part of the group
# use dictionary
# O(n)

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: # edge case
            return "Zero"
        str_num = str(num) # "1234567"
        group = [] # create a group to put digits into it
        i=len(str_num)-1

        while i>=0: # create something like ['12','345','678']
            count = 0
            temp = ''
            while i>=0 and count <3:
                temp+=str_num[i]
                i -= 1
                count+=1
            temp=temp[::-1] # '876' need reverse to '678'
            group.append(temp[:]) # need copy! "temp[:]"
        group.reverse() # ['678','345','12'] need reverse to ['12','345','678']

        # print group
        dict_ge = {'0':'','1':'One ','2':'Two ','3':'Three ','4':'Four ','5':'Five ','6':'Six ','7':'Seven ','8':'Eight ','9':'Nine '}
        dict_yi = {'1':'Eleven ','2':'Twelve ','3':'Thirteen ','4':'Fourteen ','5':'Fifteen ','6':'Sixteen ','7':'Seventeen ','8':'Eighteen ','9':'Nineteen ','0':'Ten '} # if middle one is '1'
        dict_shi = {'2':'Twenty ','3':'Thirty ','4':'Forty ','5':'Fifty ','6':'Sixty ','7':'Seventy ','8':'Eighty ','9':'Ninety '}
        dict_wei = {"0":'','1':"Thousand ",'2':"Million ","3":"Billion "}
        res = ''
        wei = len(group)-1

        for i in range(0,len(group)):
            part = group[i]

            if len(part) != 3: # The beginning part of the number may have less then three digits
                if len(part) == 2: # If two digits
                    if part[0] == '1': # If something like "teen"
                        res+=dict_yi[part[1]]
                    else: # if normal
                        res = res + dict_shi[part[0]] + dict_ge[part[1]]
                else: # len(part) == 1:
                    res += dict_ge[part[0]] # just add one digit number

            else: # normal
                if part[0]!= '0': # because if less than one hundred, we should not add 'hundred' to it
                    res = res + dict_ge[part[0]] + "Hundred "
                if part[1] == '1': # if something like "teen"
                    res+=dict_yi[part[2]]
                elif part[1] == '0': # if zero, go to the last digit
                    res = res + dict_ge[part[2]]
                else: # general situation
                    res = res + dict_shi[part[1]] + dict_ge[part[2]]

            if int(part)!=0: # because if zero, we shouldn't add "million" or the like to it.
                res += dict_wei[str(wei)]
            wei -=1 # track which part of the number we are dealing with

        return res[:-1]  # get rid of the last space
c=Solution()
# print c.numberToWords(12345678)
# print c.numberToWords(0)
# print c.numberToWords(1000000)
# print c.numberToWords(112)
# print c.numberToWords(11000001)
# print c.numberToWords(100100)