#1
n=5
num=1
for i in range(n):
    for j in range(i):
        print(num, end=" ")
        num=num+1
    print("\n")

#2
n=5
s=2*(n-1)
for i in range(n):
    for j in range(i):
        print(j+1, end=" ")
    for j in range(s):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print(j, end=" ")
    print("\n")
    s=s-2

#3
n=5
k=65
for i in range(n):
    for j in range(i):
        print(chr(k), end=" ")
        k=k+1
    print("\n")

#4
n=5
for i in range(n):
    k=65
    for j in range(i):
        print(chr(k), end=" ")
        k=k+1
    print("\n")

#5
n=5
for i in range(n,0,-1):
    k=65
    for j in range(i):
        print(chr(k), end="")
        k=k+1
    print("\n")

#6
n=5
k=65
for i in range(n,0,-1):
    for j in range(i):
        print(chr(k), end="")
        
    print("\n")
    k=k+1

#7
n=5
k=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(k), end="")
        
    print("\n")
    k=k+1

#8
n=5
for i in range (n):
    k=65
    for j in range (n-i-1):
        print(" ", end="")
    for j in range (2*i+1):
        print(chr(k), end="")
        k=k+1
        
    print("\n")

#9 
n=5
for i in range (n):
    k=65
    for j in range (n-i-1):
        print(" ", end="")
    for j in range (i):
        print(chr(k), end="")
        k=k+1
    for j in range(i,-1,-1):
        k=65
        print(chr(k+j),end="")
        
    print("\n")

#10
n=5
k=65+n
for i in range(0,n+1):
    for j in range(i,-1,-1):
            print(chr(k-j), end="")
            
    print("\n")

#11
n=5
k=65+n
for i in range(0,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print(chr(k-j), end="")
    for j in range(i,-1,-1):
            print(chr(k-j), end="")
            
    print("\n")

#12
n=5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print("\n")
    
for k in range(n):
    for j in range(k):
        print("*", end="")
    print("\n")
