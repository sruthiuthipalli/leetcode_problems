class Solution:
    def reverse(self, x: int) -> int:
        temp=x
        r=0
        if temp<0:temp=abs(temp)
        while(temp!=0):
            d=temp%10
            r=r*10+d
            temp=temp//10
        if(r>=(2**31)-1):return 0
        elif x<0:return -1* r
        else:return r

       
       