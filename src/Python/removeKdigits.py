class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        st = list()
        for n in num:
            while st and k and st[-1] > n:
                st.pop()
                k -= 1
            
            if st or n is not '0': 
                st.append(n)
            
        if k > 0:
            st = st[:-k]

        return ''.join(st) or '0'