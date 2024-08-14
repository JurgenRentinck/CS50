def main():
    yell("This", "is",  "CS50")


def yell(*words):
    #list comprehension as alterntive from map
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()