# use program mypy

#type hint
def miauw(n: int) -> str:
    return "Miauw\n" * n


number: int = int(input("Number: "))
miauws: str = miauw(number)
print(miauws, end="")