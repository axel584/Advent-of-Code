class Solution:

    def isSorted(self,s) :
        for i in range(1,len(s)):
            if s[i]<s[i-1] :
                return False
        return True

    def makeStringSorted(self, s: str) -> int:
        nbOperation = 0
        chaine = list(s)
        while not self.isSorted(chaine) :
            i = len(chaine) - 1
            print("debut i",i)
            while chaine[i]>=chaine[i-1] and i>=1:
                print("milieu i",i)
                i -= 1
            print("i",i)
            j = len(chaine) - 1
            while chaine[j]>s[i-1] and j>=1:
                j -= 1
            print("j",j)
            temp = chaine[j]
            chaine[j] = chaine[i-1]
            chaine[i-1] = temp
            print("chaine",chaine)
        return nbOperation



s = Solution()
assert s.makeStringSorted('cba') == 5
#assert s.makeStringSorted('aabaa') == 2
