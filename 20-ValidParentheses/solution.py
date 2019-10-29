"""
Key Points:
    1. Use a Stack to solve this problem.
    2. Stack is data structure, like List or Set, which you already know.
    3. To understand what is a Stack, you can image it is a box, and the
    number(or other data) you want to put in are books. The box is small,
    so every time you can only put one book in. But the box is deep, so
    you can put one book on top of another. So, you can only do two types
    of operations to the box: [1] put one book on top of the current book;
    [2] get the toppest book out. So, using stack only allows you to operate
    on the most recent element in it.
    4. In practice, you can use a List as a Stack. The append() is add one
    into it, the pop() is remove the last one. You can check the website
    https://www.w3schools.com/python/python_lists.asp for all methods for
    list.
    5. For this question, the key point to solve it is, when you see a right
    parenthesis, namely ')' or ']' or '}', you will want to check whether
    the last parenthesis is a cooresponding left parenthesis. If they match,
    we just remove both from the stack and keep checking.
    6. We also used a Map in the code. Map is also a data structure.
    7. Map is used to store pairs. Every pair has a key and a value. You can
    use 'in' to check whether a Map contains a key. If it does, you can use
    map[key] to get the corresponding value.
    8. In the code, we use Map to store the mapping from left parenthesis to
    right parenthesis. This can make the code look cleaner. Otherwise, you
    need to write a multi-layer if-else statements to check whether a right
    parenthesis match one left parenthesis.
    9. If you are going to explain this, how stack is used and why map can
    improve the readability of the code, and some corner cases will be the
    most important things.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] # use a list as a Stack
        match_map = {'(': ')', '[': ']', '{': '}'} # use a map to store the mapping
        for ch in s: # iterate each char in the given string from left to right
            if ch in match_map: # this means: if ch is a left parenthesis
                stack.append(ch) # then push it to the stack (append to the end of the list)
            else: # if it is a right parenthesis, here we assume the string only contains parentheses
                if len(stack) == 0: # if no left parenthesis appeared before, definitely not match
                    return False
                last_in = stack.pop() # if there is one, get it and remove it from the list
                if ch != match_map[last_in]: # check whether it match
                    return False
        return len(stack) == 0 # check whether there are extra left parentheses left(e.g. imagine the case: '[[]' )
