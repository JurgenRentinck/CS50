def main():
    yell("This", "is",  "CS50")


def yell(*words):
    #map makes sure function upper in class str is executed on each
    #word in the list
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()