def f(*args, **kwargs):
    print("Positional", args)
    print("Named", kwargs)

#example how print would look like
#def print(*objects, end="", sep="" )


f(10,50,25,5,gold=100,silver=299,bronze=933)