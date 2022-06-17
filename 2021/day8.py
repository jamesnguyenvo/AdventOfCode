def part1(text): 
    with open("input.txt") as textInput:
        signal = []
        output = []

        for line in textInput.read().strip().split('\n'):
            left = [x for x in line.split('|')[0].split()]
            right = [x for x in line.split('|')[1].split()]
            signal.append(left)
            output.append(right)
        
        d1,d4,d7,d8 = 0, 0, 0, 0
        
        for line in output:
            for letters in line:
                if len(letters) == 2:
                    d1 += 1
                elif len(letters) == 4:
                    d4 += 1
                elif len(letters) == 3:
                    d7 += 1
                elif len(letters) == 7:
                    d8 += 1
        print(d1+d4+d7+d8)
       

def part2(text):
    with open("input.txt") as textInput:
        #actual input
        
        signal = []
        output = []
        total = 0
       
        for line in textInput.read().strip().split('\n'):
            left = [x for x in line.split('|')[0].split()]
            right = [x for x in line.split('|')[1].split()]
            signal.append(left)
            output.append(right)

        '''
        #test input
        signal = [["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"], ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]]
        output = [["cdfeb", "fcadb", "cdfeb", "cdbaf"], ["cdfeb", "fcadb", "cdfeb", "cdbaf"]]
        '''

        # for line in signal:
        for i in range(len(signal)):
            dig = {}
            for letters in signal[i]:
                if len(letters) == 2:
                    dig[1] = letters
                elif len(letters) == 4:
                    dig[4] = letters
                elif len(letters) == 3:
                    dig[7] = letters
                elif len(letters) == 7:
                    dig[8] = letters
            # print(dig)

            for letters in signal[i]:
                #2,3,5 have length 5
                #compare the letters with 4, 7
                if len(letters) == 5:
                    if getOverlap(letters, dig[4]) == 2 and getOverlap(letters, dig[7]) == 2:
                        dig[2] = letters
                    elif getOverlap(letters, dig[4]) == 3 and getOverlap(letters, dig[7]) == 3:
                        dig[3] = letters
                    elif getOverlap(letters, dig[4]) == 3 and getOverlap(letters, dig[7]) == 2:
                        dig[5] = letters
                #0,6,9 have length 6
                #compare with 4, 7
                elif len(letters) == 6:
                    if getOverlap(letters, dig[4]) == 3 and getOverlap(letters, dig[7]) == 3:
                        dig[0] = letters
                    elif getOverlap(letters, dig[4]) == 3 and getOverlap(letters, dig[7]) == 2:
                        dig[6] = letters
                    elif getOverlap(letters, dig[4]) == 4 and getOverlap(letters, dig[7]) == 3:
                        dig[9] = letters
            # print("new digits: ", dig)

            outputDigits = ""
            for letters in output[i]:
                for digit, pattern in dig.items():
                    if sorted(pattern) == sorted(letters):
                        # print(digit)
                        outputDigits += str(digit)
            # outputDigits = outputDigits[:len(outputDigits)//2]
            total += int(outputDigits)
        print(total)
        
def getOverlap(letters1, letters2):
    commonLetters = 0
    for letter in letters1:
        if letter in letters2:
            commonLetters += 1
    return commonLetters

part2("input.txt")
