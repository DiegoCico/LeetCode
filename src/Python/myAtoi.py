class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        integer = ""
        for i in s:
            if (i == "-" or i == "+") and not integer:
                integer += str(i)
            elif i.isdigit():
                integer += str(i)
            else:
                break

        try:
            result = int(integer)
        except:
            result = 0

        return max(-2**31, min(result, 2**31 - 1))

