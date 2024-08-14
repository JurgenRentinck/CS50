#def main():
#    print("Miauw")
#    print("Miauw")
#    print("Miauw")


#def main(m):
#    n = 1
#    while n <= m:
#        print("Miauw") 
#        n += 1


def main(m):
    while m != 0:
        print("Miauw") 
        m -= 1

def main2(m):
    #for i in [0,1,2]:
    #for i in range(m):
    for _ in range(m):
        print("Miauw2")

#niet zo goed
def main3(n):
    print("Miauw3\n" * n,end="")

#get user input
def getInput():
    while True:
        n = int(input("What is n?"))
        if n > 0:
            #break
            return n

n = getInput()
main(n)
main2(n)
main3(n)