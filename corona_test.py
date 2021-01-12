age = (input("Are you a cigarette addict older than 75 years old? Yes/No ")).lower() == "yes"
chronic = (input("Do you have a severe chronic disease? Yes/No ")).lower() =="yes"
immune = (input("Is your immune system too weak? Yes/No ")).lower() =="yes"

if age and chronic and immune:
  print("You are in risky group!!!")
else:
  print("You are not in risky group.")