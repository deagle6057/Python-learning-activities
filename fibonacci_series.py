fibonacci_list=[]
a,b=1,1
count=0
while True:
  fibonacci_list.append(a)
  c=a+b
  a=b
  b=c
  if fibonacci_list[-1]>=55:
    print(fibonacci_list)
    break
  count+=1