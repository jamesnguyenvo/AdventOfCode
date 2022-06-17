def part1(text):

    with open(text, "r") as textInput:

        movement = textInput.read().split("\n")
        movement.pop()

        #horizontal, depth, aim
        calculatedDist = [0,0,0]

        for move in movement:

            direction = move.split(' ')[0]
            distance = int(move.split(' ')[1])
            
            if direction == "forward":
                calculatedDist[0] += distance
                calculatedDist[1] += (calculatedDist[2] * distance)
            elif direction == "up":
                #calculatedDist[1] -= distance
                calculatedDist[2] -= distance
            elif direction == "down":
                #calculatedDist[1] += distance
                calculatedDist[2] += distance
            
        return (calculatedDist[0]*calculatedDist[1])
print(part1("input.txt"))
    