def checkArmstrong(n):
    #write your code here !!!!!!!!!
    temp=n
    temp1=n
    count=0
    arm=0
    while(temp>0):
        count+=1
        temp=temp//10

    while(temp1>0):
        a=temp1%10
        arm=arm+(a**count)
        temp1=temp1//10

    if (arm==n):
        return 'true'
    else:
        return 'false'
    
n=int(input("Enter a number"))
print(checkArmstrong(n))