#x = input("What is x? ")
#y = input("What is y? ")

#z = int(x) + int(y)

#print(z)

#x = int(input("What is x? "))
#y = int(input("What is y? "))
#x = float(input("What is x? "))
#y = float(input("What is y? "))
#z = round((x + y),0)
#print(f"{z:,}")

def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
    return n ** 2

main()
