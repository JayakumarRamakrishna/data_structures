#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 16:38:14 2021

@author: jramakrishna
"""
from collections import deque

# problem statement - design an algorithms with breadth-first search that is able to find the shortest path from a given source to a given destination. 
# The maze is represented by a two-dimensional list.
# The (0,0) is the source and (4,4) is the destination. 0 represents walls or obstacles and 1 is the valid cells we can include in the solution.


class MazeSolver:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float('inf')
        
    def is_valid(self, row, col):
        
        # outside the table horizontally
        if row < 0 or row >= len(self.matrix):
            return False
        
         # outside the table vertically
        if col < 0 or col >= len(self.matrix):
            return False
        
        # Obstacle
        if self.matrix[row][col] == 0:
            return False
        
        # Already visited
        if self.visited[row][col]:
            return False
        
        return True
    
    def search(self, i, j, destination_x, destination_y):
        self.visited[i][j] = True
        # queue implemented using doubly linked list - O(1) for first & last item
        queue = deque()
        # i - x coordinate
        # j - y coordinate
        # d - distance
        queue.append((i,j,0))
        
        while queue:
            
            # take the first item inserted
            (i,j,dist) = queue.popleft()
            
            # If we reached the destination - found min_distance
            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break
            
            # move  - L, U, R, D
            for move in range(len(self.move_x)):
                # Calculate the position after move
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]
                
                #check the posibility of move with coordinates (next_x, next_y)
                if self.is_valid(next_x,next_y):
                    # Make the given move (BFS)
                    self.visited[next_x][next_y]= True
                    
                    # Append the given move to queue
                    queue.append((next_x,next_y, dist + 1))
              
                
    def show_results(self):
        if self.min_distance != float('inf'):
            print('min destination is : ', self.min_distance)
        else:
            print("can't reach destination")
      
        
if __name__ == '__main__':
    m = [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
        ]
    maze_solver = MazeSolver(m)
    maze_solver.search(0, 0, 4, 4)
    maze_solver.show_results()
        