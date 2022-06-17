def part1(text):
    
    with open(text, "r") as textInput:

        lines = textInput.read().split("\n\n")
        #sequence of bingo nums called
        nums = [int(num) for num in lines[0].split(",")]
        boards = []
        lines = lines[1:]
        
        #formatting input
        for line in lines:
            rows = line.split('\n')
            board = []
            for currentRow in rows:
                row = [int(num) for num in currentRow.split()]
                board.append(row)
            boards.append(board)
        boards[-1].pop()

        bingo = False
        for num in nums:
            if not bingo:
                for table in boards:
                    for row in table:
                        for i in range(len(row)):
                        #print(table[i][0])
                            if row[i] == int(num):
                                row[i] = -1
                                #print("here")
                for table in boards:
                    if checkWin(table):
                        bingo = True
                        #print("how'd i get in here")
                        #print(table)
                        total = calculateTotal(table, num)
                        
            else:
                break
        return nums
        #print(total)

def part2(text):
    
    with open(text, "r") as textInput:

        lines = textInput.read().split("\n\n")
        #sequence of bingo nums called
        nums = [int(num) for num in lines[0].split(",")]
        boards = []
        lines = lines[1:]
        
        #formatting input
        for line in lines:
            rows = line.split('\n')
            board = []
            for currentRow in rows:
                row = [int(num) for num in currentRow.split()]
                board.append(row)
            boards.append(board)
        boards[-1].pop()
        done = False
        
        '''
        for num in nums:
            if not done:
                for table in boards:
                    for row in table:
                        for i in range(len(row)):
                            if row[i] == int(num):
                                row[i] = -1
                newBoards = []
                for board in boards:
                    if checkWin(board):
                        if len(boards) == 1:
                            print(board, num)
                            #print(calculateTotal(board, num))
                            done = True
                    else:
                        newBoards.append(board)
                boards = newBoards
            else:
                break
        #print(boards)
        '''  
        for num in nums:
            if not done:
                for table in boards:
                    for row in table:
                        for i in range(len(row)):
                            if row[i] == int(num):
                                row[i] = -1
                #check if each board is finished
                count = 0
                while count < len(boards):
                    if checkWin(boards[count]):
                        if len(boards) > 1:
                            boards.remove(boards[count])
                            #print(len(boards))
                        else:
                            # last one
                            done = True
                            #print(boards[count], num)
                            print(calculateTotal(boards[count], num))
                            break
                    else:
                        #print("here")
                        count += 1
            else:
                break
       
def calculateTotal(table, lastCalledNum):
    total = 0
    for row in table:
        for num in row:
            #print(num)
            if num >= 0:
                total += num
            
    return total*lastCalledNum
    
def checkWin(table):
    #horizontal
    for row in table:
        win = True
        for i in range(5):
            if row[i] != -1:
                win = False
                break
        if win:
            #print("horizontal win")
            return win
    #vertical
    for i in range(5):
        win = True
        for j in range(5):
            if (table[j][i]) != -1:
                win = False
                break
        if win:
            #print("vertical win")
            return win

    return win

part2("input.txt")

