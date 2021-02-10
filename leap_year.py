x=int(input("Please enter a year with 4 digits:"))

if x%4==0:
  if x%100==0:
    if x%400==0:
      print(f"{x} is a leap year")
    else:
      print(f"{x} is not a leap year")
  else:
   print(f"{x} is a leap year")
else:
  print(f"{x} is not a leap year")