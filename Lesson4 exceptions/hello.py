


#def main():
    #syntax erros cannot be catched, you need to
    #solve them yourself.
    # print("Hello, world)

def main2():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("This is not a valid int")
        else:          
            break

    print(f"x is {x}")        


def main3():
    x = get_int("What is x? ")
    print(f"x is {x}")        

def get_int(caption):
    while True:
        try:
            return int(input(caption))
        except ValueError:
            pass
        
#raise an expection? 

#main()
#main2()
main3()