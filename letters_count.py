sentence =input("Please enter your sentence:")

x=list(sentence)
y=list(set(sentence))
letters_dict={}

for i in y:
  letters_dict[i]=x.count(i)
print(letters_dict)
