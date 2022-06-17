def part1(text):

    with open(text, "r") as textInput:
        
        binaryNums = textInput.read().split("\n")
        binaryNums.pop()

        gamma = ""
        epsilon = ""

        for i in range(len(binaryNums[0])):
            
            one = len([line for line in binaryNums if line[i] == "1"])
            zero = len([line for line in binaryNums if line[i] == "0"])
         
            if zero < one:
                gamma += "1"
                epsilon += "0"
            elif zero > one:
                gamma += "0"
                epsilon += "1"
       
        return int(gamma, 2) * int(epsilon, 2)
    
def part2(text):
    
 
    with open(text, "r") as textInput:
        
        binaryNums = textInput.read().split("\n")
        binaryNums.pop()

        oxygenList = binaryNums.copy()
        co2List = binaryNums.copy()

        print(int(getOxygen(oxygenList)[0], 2) * int(getCo2(co2List)[0], 2))
        
        
def getOxygen(numsList):
    #oxygen rating
    for i in range(len(numsList[0])):
        if len(numsList) > 1:
            zeroCount = len([line for line in numsList if line[i] == "0"])
            oneCount = len([line for line in numsList if line[i] == "1"])

            if oneCount >= zeroCount:
                for num in numsList:
                    #print("1 larger in index: ", i, numsList)
                    numsList = [line for line in numsList if line[i] == "1"]
                    #print("removed: ", numsList)
            else:
                #print("0 larger in index: ", i, numsList)
                numsList = [line for line in numsList if line[i] == "0"]
                #print("removed: ", numsList)
                
    return numsList

def getCo2(numsList):
    #co2 rating
    for i in range(len(numsList[0])):
        if len(numsList) > 1:
            zeroCount = len([line for line in numsList if line[i] == "0"])
            oneCount = len([line for line in numsList if line[i] == "1"])
            
            if oneCount >= zeroCount:
                for num in numsList:
                    numsList = [line for line in numsList if line[i] == "0"]
            else:
                numsList = [line for line in numsList if line[i] == "1"]
    
    return numsList


part2("input.txt")
    