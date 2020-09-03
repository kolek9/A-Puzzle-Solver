#Kole Keeney
#AI Program 1

import numpy as np
from heapq import heappush, heappop

class Node:
    def __init__(self,tiles,level = 0,parent = None): #initialize Nodes
        self.tiles = tiles
        self.level = level
        self.parent = parent

    def __lt__(self, other):
        return self.f() < other.f()

    def generate_child(self):
        i = self.tiles.index('0')
        if i in [4,5,6,7,8,0]: #if 0 is in the bottom, move 'up' 1 by going left 3
            try:
                child = self.tiles[:]
                temp = child[i]
                child[i] = child[i-3]
                child[i-3] = temp
                yield Node(child, self.level+1,self)
            except IndexError as error:
                pass
        if i in [2,3,5,6,8,0]: #if 0 is on right move left one
            try:
                child = self.tiles[:]
                temp = child[i]
                child[i] = child[i-1]
                child[i-1] = temp
                yield Node(child, self.level+1,self)
            except IndexError as error:
                pass
        if i in [1,2,4,5,7,8]: #if 0 is on the left move right one
            try:
                child = self.tiles[:]
                temp = child[i]
                child[i] = child[i+1]
                child[i+1] = temp
                yield Node(child, self.level+1,self)
            except IndexError as error:
                pass
        if i in [1,2,3,4,5,6]: #if 0 is on top, move 'down' 1 by going right
            try:
                child = self.tiles[:]
                temp = child[i]
                child[i] = child[i+3]
                child[i+3] = temp
                yield Node(child, self.level+1,self)
            except IndexError as error:
                pass


    def move(self,tiles,x1,y1,x2,y2): #move puzzle tiles around using temps
        if x2 >= 0 and x2 < 3 and y2 >= 0 and y2 < 3: #maybe 9
            temp = []
            temp = self.copy(tiles)
            temp2 = temp[x2][y2]
            temp[x2][y2] = temp[x1][y1]
            temp[x1][y1] = temp2
            return temp
        else:
            return None
        
    def copy(self,root): #create second identical list
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def f(self): #calculate f score by adding manhattan + level
        goal = [1,2,3,4,5,6,7,8,0]
        count = 0
        for i in range(9):
            if (self.tiles[i] != goal[i]) and (self.tiles[i] != '0'):
                count += 1
        return count + self.level
        

class Queue: #Priority queue class
  def __init__(self):
    self.pq = []

  def add(self, item):
    heappush(self.pq, item)

  def remove(self, item):
    value = self.pq.remove(item)
    heapify(self.pq)
    return value is not None

  def __len__(self):
    return len(self.pq)


class Answer:
    def __init__(self, initial = None):
        self.initial = Node(initial)
        
    def output_path(self, end): #creates path by accessing each node's parent
        path = [end]
        nexxt = end.parent
        while nexxt:
            path.append(nexxt)
            nexxt = nexxt.parent
        return path

    def solution(self):
        queue = []
        heappush(queue, self.initial)
        dead = set()
        level = 0
        while queue:
            current = heappop(queue)
            if current.tiles[:-1] == [1,2,3,4,5,6,7,8,0]:
                path = self.output_path(current)
                for node in reversed(path):
                    print(node)
                moves = len(path)
            for node in current.generate_child():
                if node not in dead:
                    heappush(queue, node)
            dead.add(current)
            

def create_board(): #reads un file and creates puzzle list
    fileName = input("What is the name of the file you'd like to use?\n")
    matrix = open(fileName).read()
    count = 0
    puzzle = []
    invalid = ['', ' ', '\n']
    for i in matrix:
        if i not in invalid and count <9:
            puzzle.append(i)
            count+=1
    return puzzle
    

def manhattan(puzzle): #counts how many tiles are in the wrong place
    goal = [1,2,3,4,5,6,7,8,0]
    count = 0
    for i in range(9):
        if (puzzle[i] != goal[i]) and (puzzle[i] != '0'):
                count += 1
    return count


puzzle = create_board()        
print(puzzle)
f = manhattan(puzzle)
print(f)

end = Answer(puzzle)
end.solution()


#algorithm
#first read in matrix
#calculate manhattan distance
#move blank space in every direction - create new nodes
#store each new node and manhattan value in queue, pop old one
#choose smallest manhattan value and continue until solution or impossible

    


        
        
