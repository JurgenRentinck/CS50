# Ask user for their name
#name = input("What's your name? ")
#"""
#Multiline comment
#"""
# Say hello to user less good variants
#print("Hello,", end="")
#print(name)
#print("Hello, " + name)
#print("Hello",name,sep=", ")

#remove spaces and capitalize the name using capitalize 
#or title (for both word firstname and lastname))
#name = name.strip().title()
#print(f"Hello, {name}")

#BEST SOLUTION
name = input("What's your name? ").strip().title()

#split name to firstname and lastname
firstname,lastname = name.split(" ")

print(f"Hello, {firstname}")