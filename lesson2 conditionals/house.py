
def main():
    name = input("Waht is you name?")

#    if name == "Harry":
#        print("A")
#    elif name == "Piet":
#        print("A")
#    elif name == "Ron":
#        print("A")
#    elif name == "Drako":
#        print("C")
#    elif name == "Arie":
#        print("D")        

    match name:
        case "Harry" | "Piet" | "Ron":
            print("A")
  #      case "Piet":
  #          print("A")
  #      case "Ron":
  #          print("A")
        case "Drako":
            print("C")
        case "Arie":
            print("D")
        case _:
            print("Who?")            


main()

