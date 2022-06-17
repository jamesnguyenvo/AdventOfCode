def part1(text): 
    with open("input.txt") as textInput:
        
        heights = [line for line in textInput.read().strip().split('\n')]
        
        
        #test input
        '''
        heights = ["2199943210",
                   "3987894921",
                   "9856789892",
                   "8767896789",
                   "9899965678"]
        '''
        sum = 0
        sizes = []

        for row in range(len(heights)):
            for col in range(len(heights[0])):
                adjacent = []
                if row-1 >= 0:
                    # print("1")
                    adjacent.append(int(heights[row-1][col]))
                if row+1 < len(heights):
                    # print("2")
                    adjacent.append(int(heights[row+1][col]))
                if col-1 >= 0:
                    # print("3")
                    adjacent.append(int(heights[row][col-1]))
                if col+1 < len(heights[0]):
                    # print("4")
                    adjacent.append(int(heights[row][col+1]))

                # print(adjacent)
                if int(heights[row][col]) < min(adjacent):
                    # print(heights[row][col])
                    sum += 1 + int(heights[row][col])

                    basin = [(row, col)]
                    # print(basin)
                    
                    for x, y in basin:
                        # print(row)
                        if x-1 >= 0 and int(heights[x-1][y]) != 9 and (x-1,y) not in basin:
                            # print("1")
                            basin.append((x-1, y))
                        if x+1 < len(heights) and int(heights[x+1][y]) != 9 and (x+1,y) not in basin:
                            # print("2")
                            basin.append((x+1, y))
                        if y-1 >= 0 and int(heights[x][y-1]) != 9 and (x,y-1) not in basin:
                            # print("3")
                            basin.append((x, y-1))
                        if y+1 < len(heights[0]) and int(heights[x][y+1]) != 9 and (x,y+1) not in basin:
                            # print("4")
                            basin.append((x, y+1))
                    # print(basin)
                    sizes.append(len(basin))
                    
         #############################          
        #                             #
        # i'm missing top right corner#
        #                             #
         ##############################
        # print(sizes)
        # print(sum)
        #want the largest three basins
        sizes.sort(reverse=True)
        print(sizes[0] * sizes[1] * sizes[2])

       
        
part1("input.txt")
