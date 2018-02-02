class Solution:
    def fibR(self, n):
        if n==1 or n==2:
          return 1
        return self.fibR(n-1)+self.fibR(n-2)

x=Solution()
print(x.fibR(6))