user_num = int(input("Please enter a number: "))
prime_list=[2, 3, 5, 7]
x=1
if user_num in prime_list:
  print(user_num,"is a prime number")
elif user_num >=10:
  for i in prime_list:
    x=x*(user_num%i)
  if x==0:
   print(user_num,"is not a prime number")
  else:
   print(user_num,"is a prime number")  
else:
  print(user_num,"is not a prime number")