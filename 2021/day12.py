# https://github.com/DecemberDream/advent-of-code/tree/main/2021/day12

from collections import defaultdict

def part1(input):
    with open(input) as textInput:
        edges = [line.split('-') for line in textInput.read().strip().split('\n')]

        neighbours = defaultdict(list)
        smallCaves = set()
        visited = set()
        '''
        for edge in edges:
            print(edge)
        '''
        for edge in edges:
            a,b = edge
            neighbours[a].append(b)
            neighbours[b].append(a)

            #find which caves we can revisit
            if a.islower():
                smallCaves.add(a)
                # print(a)
            if b.islower():
                # print(b)
                smallCaves.add(b)
        # print(neighbours)
        print(dfs("start", visited, neighbours, smallCaves))        

def dfs(currentNode, visited, neighbours, smallCaves):
    if currentNode in visited:
        return 0
    if currentNode == "end":
        return 1
    if currentNode in smallCaves:
        visited.add(currentNode)
    
    paths = 0
    '''
    if currentNode == "start":
        print(neighbours[currentNode])
    '''
    for node in neighbours[currentNode]:
        paths += dfs(node, visited, neighbours, smallCaves)
        
    visited.discard(currentNode)
    # print(visited)
    return paths

part1("input.txt")
