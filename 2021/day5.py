from collections import Counter

def part1(text):
    

    with open(text, "r") as textInput:

        lines = textInput.read().strip().split("\n")
        board = []
     
        for line in lines:
            x1 = int(line.split()[0].split(',')[0])
            y1 = int(line.split()[0].split(',')[1])
            x2 = int(line.split()[2].split(',')[0])
            y2 = int(line.split()[2].split(',')[1])

            if x1 == x2 or y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    #print(x)
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        #print([x,y])
                        board.append((x,y))

        #print(Counter(board).items())
        overlap = 0
        for (x,y) in Counter(board).items():
            #print(x,y)
            if y > 1:
                #print(x,y)
                overlap += 1
        print(overlap)

def part2(text):
    

    with open(text, "r") as textInput:

        lines = textInput.read().strip().split("\n")
        board = []
     
        for line in lines:
            x1 = int(line.split()[0].split(',')[0])
            y1 = int(line.split()[0].split(',')[1])
            x2 = int(line.split()[2].split(',')[0])
            y2 = int(line.split()[2].split(',')[1])
            
            #direction
            if x2 > x1:
                dx = 1
            elif x2 < x1:
                dx = -1
            if y2 > y1:
                dy = 1
            elif y2 < y1:
                dy = -1

            if x1 == x2:
                dx = 0
            if y1 == y2:
                dy = 0

            #x1,y1
            board.append((x1,y1))

            while x1 != x2 or y1 != y2:
                #x1,y1 to x2,y2
                x1 += dx
                y1 += dy
                board.append((x1,y1))

        #print(board)
        overlap = 0
        for (x,y) in Counter(board).items():
            if y > 1:
                #print(x,y)
                overlap += 1
        print(overlap)

part2("input.txt")

