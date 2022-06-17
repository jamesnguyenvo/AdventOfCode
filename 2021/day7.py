def part1(text): 
    with open("input.txt") as textInput:
        nums = [int(x) for x in textInput.read().strip().split(',')]
        nums.sort()

        mid = nums[len(nums)//2]
        fuel = 0
        for num in nums:
            fuel += abs(num-mid)
      
        print(fuel)

def part2(text):
    with open("input.txt") as textInput:
        nums = [int(x) for x in textInput.read().strip().split(',')]
        #nums.sort()


        # mid = nums[len(nums)//2]
        # fuel = 0
        
        '''
        dists = [abs(num - mid) for num in nums]
        for x in dists:
            fuel += x*(x+1)//2
        #print(sum([x*(x+1)//2 for x in dists]))
        print(fuel)
        '''
        '''
        for num in nums:
            fuel += incrFuel(abs(num-mid))
            
        for mid in range(min(nums), max(nums)+1):
            fuel = min(fuel, sum(incrFuel(abs(x-mid)) for x in nums))
        '''
        best = 999999999

        for i in range(len(nums)):
            score = 0
            for num in nums:
                fuel = abs(num-i)
                score += incrFuel(fuel)
            if score < best:
                best = score

        print(best)


def incrFuel(fuel):
    return fuel*(fuel+1)//2

part2("input.txt")
