


def main():
    n = int(input("How many sheep?"))
    for i in sheep(n):
        print(i)

def sheep(n):
    for i in range(n):
        #return per itteration
        yield "--sheep--" * i



if __name__ == "__main__":
    main()



