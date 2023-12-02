class Solution:
    convertion = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    def romanToInt(self, s: str) -> int:
        somme = 0
        precedent = ''
        for c in s :
            if precedent != '' and Solution.convertion[precedent]<Solution.convertion[c] : # cas des soustractions
                somme -= Solution.convertion[precedent]*2
            somme += Solution.convertion[c]
            precedent = c
        return somme


s = Solution()
assert s.romanToInt('III') == 3
assert s.romanToInt('LVIII') == 58
assert s.romanToInt('MCMXCIV') ==1994