class Solution:
    def countPrimes(self, n: int) -> int:
        import math
        arr=[True]*n
        if n > 0:
            arr[0]=False
        if n>1:
            arr[1]=False
        size=int(math.sqrt(n))
        for i in range(2,size+1):
            if arr[i]==True:
                for j in range(i*i,n,i):
                    arr[j]=False
        primes=[]
        for i in range(len(arr)):
            if arr[i]==True:
                primes.append(i)
        return len(primes)