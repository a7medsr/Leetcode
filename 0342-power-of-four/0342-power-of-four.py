class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        def rec(x):
            if x>n:
                return False
            elif n==x:
                return True
            return  rec(x*4)
        return rec(4)

        