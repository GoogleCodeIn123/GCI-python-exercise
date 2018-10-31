for x in range(10):
    print("GCI is great!")
print()
name = input("What is your name?")
print("Hello " + name + ", pleased to meet you.")
rev_name = ""
index = len(name)
while index > 0 :
    rev_name = rev_name + name[index-1]
    index = index - 1
print("Did you know that your name backwards is " + rev_name + "?")


