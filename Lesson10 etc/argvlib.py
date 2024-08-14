import argparse


parser = argparse.ArgumentParser(description="Miauw like a cat")
parser.add_argument("-n", default=1, help="Number of times to miauw", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("Miauw")


