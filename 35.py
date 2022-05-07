class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                st.append(i)
            else:
                if len(st) == 0 and (i == ')' or i == ']' or i == '}'):
                    return False
                else:
                    if st[-1] == '(' and i == ')':
                        st.pop()
                    elif st[-1] == '{' and i == '}':
                        st.pop()
                    elif st[-1] == '[' and i == ']':
                        st.pop()
                    else:
                        return False
        if len(st) == 0:
            return True
        else:
            return False
