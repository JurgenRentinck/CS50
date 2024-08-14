#unpack coins by using * sign before the list
# and use ** for a dict

def total(gold,silver,bronze):
    return (gold * 17 + silver) * 29 + bronze

#list solution
#coins = [100,50,25]
#print(total(*coins), "Knuts")

coins = {"gold": 100,"silver": 10,"bronze": 25}
print(total(**coins), "Knuts")
