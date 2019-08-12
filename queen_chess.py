import numpy as np

class Solver():
    def __init__(self, dim):
        self.dim = dim
        self.queen_pos = [] #saves x and y coordinate of each queen
        self.solution_map = np.zeros((dim, dim))
        
        #I found 5 different patterns to place queens depending of dimension
        
        if dim%2 != 0 and dim%3 != 0:     #  5 7    11  13      17  19      23  25
            self.sol__not_mod2_and_not_mod3()
        if dim%2 == 0 and (dim-2)%3 != 0: # 4 6   10  12      16  18      22  24
            self.sol__mod2_and_not_m2_mod3()
        if (dim-2)%6 == 0:                #     8         14          20          26
            self.sol__m2_mod6()
        if (dim-9)%12 == 0:               #      9                      21
            self.sol__m9_mod12()
        if (dim-3)%12 == 0:               #                 15                      27
            self.sol__m3_mod12()
        
        for i in self.queen_pos: #put queen in board
            self.solution_map[i[0], i[1]] = 1
        self.print_map()
        
    def print_map(self):
        for i in self.solution_map:
            res = "|"
            for j in i:
                res += " " if j == 0 else "X"
            res += "|"
            print(res)
        print("-"*(self.dim+2))
    
    #putting queens like stairs means that queen placement follows this pattern :
    # +1,+1,+1 for x and +2,+2,+2 for y
    
    #put queens like stairs starting at 0,0
    def sol__not_mod2_and_not_mod3(self):
        for i in range(0,self.dim):
            self.queen_pos.append([i,(i*2)%(self.dim)])
    
    #put queens like stairs starting at 0,1
    def sol__mod2_and_not_m2_mod3(self):
        for i in range(0,self.dim):
            self.queen_pos.append([i,(i*2+1)%(self.dim+1)])
    
    #put half queens like stairs starting at 0,1
    #put 3 queens at specific location
    #put the rest like stairs starting at queen//2+2,6
    def sol__m2_mod6(self):
        for i in range(0,self.dim//2):
            self.queen_pos.append([i,(i*2+1)%(self.dim+1)])
        self.queen_pos.append([self.dim//2+1,0])
        self.queen_pos.append([self.dim//2,2])
        self.queen_pos.append([self.dim-1,4])
        for i in range(self.dim//2+3, self.dim):
            self.queen_pos.append([i-1,(i*2+1)%(self.dim+1)])
        return 1
    
    #put half queens minus 1 like stairs starting at 0,2
    #put two queens at specific location
    #put the rest with this pattern : -1,+3,-1,+3,-1 for x and +2,+2,+2 for y starting at queen//2+1,2
    def sol__m9_mod12(self):
        for i in range(0,self.dim//2-1):
            self.queen_pos.append([i,i*2+2])
        self.queen_pos.append([self.dim//2-1,0])
        self.queen_pos.append([self.dim-1,self.dim-1])
        for i in range(0, self.dim//2):
            self.queen_pos.append([(i-(i%2)+(i-1)%2)+self.dim//2,i*2+1])
        return 1
    
    #put half queens like stairs starting at 0,2
    #put one queen at specific location
    #put the rest with this pattern : -1,+3,-1,+3,-1 for x and +2,+2,+2 for y starting at queen//2+1,2
    def sol__m3_mod12(self):
        for i in range(0,self.dim//2):
            self.queen_pos.append([i,i*2+2])
        self.queen_pos.append([self.dim-2,0])
        for i in range(0, self.dim//2):
            self.queen_pos.append([(i-(i%2)+(i-1)%2)+self.dim//2,i*2+1])
        return 1
