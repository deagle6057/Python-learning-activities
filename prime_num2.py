n=int(input("Please enter a number:\n"))
prime_nums=[]
pivot_list=[2,3,5,7]
for i in range(2,n+1):
  if i <=10:
    if i in pivot_list:
      prime_nums.append(i)
  elif i > 10:
    for j in pivot_list:
      if (i%j)==0:
        break
    else:
      prime_nums.append(i)
print(prime_nums)