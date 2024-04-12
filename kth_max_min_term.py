n=int(input("enter how many numbes u want to enter in the array: "))
queue=[]
for i in range(0,n):
    ele=int(input("enter the term: "))
    queue.append(ele)

max_term=max(queue)
queue.pop(-1)
min_term=min(queue)
queue.pop(0)

q1=max(queue)
q2=min(queue)
print("maximum term in the array is:", q1)
print("manimum term in the array is:", q2)