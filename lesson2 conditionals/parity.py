



def main():
    x = int(input("Give a number: "))

    if is_even(x):
        print("Even")
    else:
        print ("Odd")

    #if x%2 == 0:
    #    print("This number is even.")
    #else:
    #    print("This number is odd")

def is_even(n):
    #if n%2 == 0:
    #    return True
    #else:
    #    return False

    #return True if n % 2 == 0 else False

    return n%2 == 0

main()