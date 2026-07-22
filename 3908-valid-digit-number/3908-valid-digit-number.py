class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        arr=[]

        while n>0:
            k=n%10
            n//=10
            arr.append(k)
        for i in range(len(arr)):
            if x==arr[i] and arr[-1]!=x:
                return True
        return False


