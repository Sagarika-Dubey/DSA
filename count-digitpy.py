def countDigits(n: int) -> int:
    count=0
    temp=n
    while(temp!=0):
        a=temp%10
        if(a!=0 and n%a==0):
            count+=1
        temp=temp//10
    return count