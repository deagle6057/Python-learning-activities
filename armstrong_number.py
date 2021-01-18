x = input("Please enter an integer number: ")
first_x=int(x)
check_x=0
power=len(x)
if not x.isdigit():
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
else:
  for i in range(0,len(x)):
    x=int(x)
    rem=x%10
    check_x+=rem**power
    x=x//10
  if check_x==first_x:
    print(first_x, "is an Armstrong number")
  else:
    print(first_x, "is not an Armstrong number")