def main():
    print_column(5)
    print_row(5)
    print_brick(10,10)

def print_column(height):
    for _ in range(height):
        print("#")    

def print_row(width):
        print("?" * width)

def print_brick(height,width):
    for _ in range(height):
        print("*" * width)

    print()
    
    #variant off the above
    for _ in range(height):
        for _ in range(width):
            print("*",end="")
        print()          

main()