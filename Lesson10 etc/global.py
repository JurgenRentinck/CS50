#GLOBAL variables can probably better be solved by classes
# global can make things very messy very fast

balance = 0

def main():
    print(f"Balance : {balance}")
    deposit(200)
    withdraw(50)
    print(f"Balance : {balance}")

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()