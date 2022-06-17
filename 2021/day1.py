def part1(text):

    with open (text, "r") as textInput:

        numbers = textInput.read().split("\n")
        numbers.pop()
        count = 0
        
        for i in range(len(numbers)-1):
            if (int(numbers[i]) < int(numbers[i+1])):
                count += 1
        
        return count


def part2(textInput):

     with open (textInput, "r") as textInput:

        numbers = textInput.read().split("\n")
        numbers.pop()
        count = 0
        '''
        end = False
        while not end:
            for i in range(len(numbers)):
                if (i+3)<len(numbers):
                    if (int(numbers[i]) + int(numbers[i+1]) + int(numbers[i+2])) < (int(numbers[i+1]) + int(numbers[i+2]) + int(numbers[i+3])):
                        #print(int(numbers[i]) + int(numbers[i+1]) + int(numbers[i+2]), int(numbers[i+1]) + int(numbers[i+2]) + int(numbers[i+3]))
                        count += 1
                else:
                    end = True

        return count
        '''

        previousWindow = None
        for i in range(len(numbers)-2):
            window = int(numbers[i]) + int(numbers[i+1]) + int(numbers[i+2])
            
            if previousWindow:
                if window > previousWindow:
                    count +=1
            previousWindow = window
        return count

print(part2("input.txt"))