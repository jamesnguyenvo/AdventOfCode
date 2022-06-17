from collections import defaultdict

def part1(text): 
    with open("input.txt") as textInput:
        nums = textInput.read().strip().split(',')
        fishes = [int(x) for x in nums]

        #print(spawnFish(80, fishes))
        print(spawnFish(256, fishes))

def spawnFish(days, fishes):
    ages = defaultdict(int)
    
    for fish in fishes:
        ages[fish] += 1

    for day in range(days):
        newAges = defaultdict(int)
        for age, amountOfFish in ages.items():
            if age > 0:
                newAges[age - 1] += amountOfFish
            else:
                newAges[6] += amountOfFish
                newAges[8] += amountOfFish
            ages = newAges
    
    return sum(ages.values())        

part1("input.txt")

