class Solution:
    def fib(self, n: int) -> int:
        def rec(num):
            if num==1:
                return 1
            elif num==0:
                return 0
            return rec(num-1)+rec(num-2)
        return rec(n)
        