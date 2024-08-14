

def miauw(n: int) -> str:
    """
    Miauws n times.

    :param n: Number of times to miauw
    :type n: int
    :raise typeError: if n is not and int
    :return: a string of n miauws, one per line
    :rtype: str
    """
    return "Miauw\n" * n


number: int = int(input("Number: "))
miauws: str = miauw(number)
print(miauws, end="")