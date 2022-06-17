# https://www.educative.io/edpresso/the-valid-parentheses-problem
def part1(text): 
    with open("input.txt") as textInput:
        
        lines = [line for line in textInput.read().strip().split('\n')]
        '''
        lines = ["[({(<(())[]>[[{[]{<()<>>",
                "[(()[<>])]({[<{<<[]>>(",
                "{([(<{}[<>[]}>{[]{[(<()>",
                "(((({<>}<{<{<>}{[]{[]{}",
                "[[<[([]))<([[{}[[()]]]",
                "[{[{({}]{}}([{[{{{}}([]",
                "{<[[]]>}<{[{[{[]{()[[[]",
                "[<(<(<(<{}))><([]([]()",
                "<{([([[(<>()){}]>(<<{{",
                "<{([{{}}[<[[[<>{}]]]>[]]"]
        '''
        scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
        scores2 = {')': 1, ']': 2, '}': 3, '>': 4}
        validChunks = {'(': ')', '{': '}', '[': ']', '<': '>'}
        
        score = 0
        scoresList = []
        '''
        for line in lines:
            newLine = deleteParentheses(line)
            for string in lines[:len(line)//2]:
                if len(newLine) > 0:
                    newLine = deleteParentheses(newLine)
            print(newLine)
        '''
        for line in lines:
            corrupted = False
            newScore = 0
            stack = []
            # print("NEW LINE")
            for char in line:
                # print("real: ", char)
                if char in validChunks.keys():
                    # print("adding")
                    # stack.append(char)
                    stack.append(validChunks[char])
                else:
                    if not stack:
                        print("shouldn't be here")
                        return
                    else:
                        top = stack[-1]
                        # print(char, top)
                        if char == top:
                            # print("found match")
                            stack.pop()
                        else:
                            # print(line + " invalid char: ", char)
                            score += scores[char]
                            corrupted = True
                            break
            # print(stack)
            if not corrupted:
                # print(stack)
                for i in range(len(stack)-1, -1, -1):
                    newScore *= 5
                    # print(i, stack[i])
                    if stack[i] in scores2:
                        newScore += scores2[stack[i]]
                        # print(newScore, stack[i])
                scoresList.append(newScore)

        scoresList.sort()
        print(scoresList[len(scoresList)//2])



def deleteParentheses(line):
    validParentheses = ['()', '{}', '[]', '<>']
    
    for parentheses in validParentheses:
        if parentheses in line:
            # print("deleting: ", parentheses)
            editedLine = line.replace(parentheses, '')
            # print("deleted: ", editedLine)
    #line without valid chunks
            return editedLine
    return line

part1("input.txt")

