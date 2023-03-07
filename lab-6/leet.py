class Solution:
    def isIsomorphic(self, s: str, t: str):
        self.s=s
        self.t=t
        set1={'1'}
        set2={'1'}
        for ch in self.s:
            set1.add(ch)
        for ch in self.t:
            set2.add('ch')
        print(set1,';',set2)
        if len(set1)==len(set2):
            return True
        else:
            return False
s=str(input())
t=str(input())
cl=Solution()
d=cl.isIsomorphic(s,t)
print(d)