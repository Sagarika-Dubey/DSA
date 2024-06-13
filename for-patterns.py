#1
n=5
for i in range (n):
    for j in range (n):
        print("*", end="")
        
    print("\n")

#2
n=5
for i in range (n):
    for j in range (i):
        print("*", end="")
        
    print("\n")

#3
n=5
for i in range (n):
    for j in range (i):
        print(j+1, end="")
        
    print("\n")

#4
n=5
for i in range (n):
    for j in range (i):
        print(i, end="")
        
    print("\n")

#5
n=5
for i in range (n,0,-1):
    for j in range (i):
        print("*", end="")
        
    print("\n")

#6
n=5
for i in range (n,0,-1):
    for j in range (i):
        print(j+1, end="")
        
    print("\n")

#7
n=5
for i in range (n):
    for j in range (n-i-1):
        print(" ", end="")
    for j in range (i+1):
        print("*", end=" ")
        
    print("\n")

#8
n=5
for i in range (n):
    for j in range (n-i-1):
        print(" ", end="")
    for j in range (2*i+1):
        print("*", end="")
        
    print("\n")

#9
n=5
for i in range (n,0,-1):
    for j in range (n-i):
        print(" ", end="")
    for j in range (i):
        print("*", end=" ")
        
    print("\n")

#10
n=5
for i in range (n,0,-1):
    for j in range (n-i):
        print(" ", end="")
    for j in range (2*i+1):
        print("*", end="")
        
    print("\n")

#11
n=5
for i in range (n):
    for j in range (n-i-1):
        
        print(" ", end="")
    for j in range (i+1):
        print("*", end=" ")
        
    print("\n")
    
    
for i in range (n,0,-1):
    for j in range (n-i):
        print(" ", end="")
    for j in range (i):
        print("*", end=" ")
        
    print("\n")


#12
n=5
for i in range(n):
    for j in range(i):
        print("*", end="")
        
    print("\n")
for k in range(n,0,-1):
    for j in range(k):
        print("*", end="")
        
    print("\n")

#13
n=6
start=1
for i in range(n):
    if i%2==0:
        start=0
    else:
        start=1
    for j in range(i):
        print(start, end="")
        start=1-start
    print("\n")