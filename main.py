""" RULES
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
import numpy as np
import os
import random
import time


class GOL:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = None
        self.running = False
        self._make_grid()


    def _make_grid(self):
        self.grid = [[(1 if random.random() < 0.15 else 0) for _ in range(self.width)] for _ in range(self.height)]

    
    def _print_grid(self):
        output_str = "\033[H"
        
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    output_str += ". "
                else:
                    output_str += "@ "
                    
            output_str += "\n"
            
        print(output_str, end="")
        

    def _clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear") 
            
    
    def run(self):
        self.running = True
        
        while self.running:
            self._clear_screen()
            self._print_grid()
            self._update_grid()
            time.sleep(0.1)
            
    def _update_grid(self):
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        
        for row in range(self.height):
            for col in range(self.width):
                neighborhood = self._get_neighborhood(row, col)
                cell_state = neighborhood[1][1]
                nb_neighbors = sum(np.array(neighborhood).flatten()) - cell_state

                if cell_state == 1 and (nb_neighbors < 2 or nb_neighbors > 3):
                    new_grid[row][col] = 0
                elif cell_state == 0 and nb_neighbors == 3:
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = cell_state
                    
        self.grid = new_grid

        
    def _get_neighborhood(self, x, y):
        neighborhood = []
        
        for dy in range(-1, 2):
            row = []
            
            for dx in range(-1, 2):
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < self.height and 0 <= ny < self.width:
                    row.append(self.grid[nx][ny])
                else:
                    row.append(0)
                    
            neighborhood.append(row)
            
        return neighborhood


def main():
    CONSTANTS = {
        "HEIGHT": 15,
        "WIDTH": 25
    }
        
    gol = GOL(CONSTANTS["WIDTH"], CONSTANTS["HEIGHT"])
    gol.run()


if __name__ == "__main__":
    main()