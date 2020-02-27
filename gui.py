import os
import math
import platform
class gui:
    D = 2 #DECIMALS
    F = "■" #The finished part
    U = "□" #The unfinished part
    clear = "cls"
    total = 100
    #total: the total steps
    #cur: the current steps that has been finished
    def display(self, cur):
        os.system(self.clear)
        bar = math.floor(cur / self.total * 100*pow(10,self.D))/pow(10,self.D) # output the percenatge
        print((str(bar) + "%").center(20))
        for j in range(math.floor(bar/10)):
            print(self.F,end = "")
        for j in range(10 - math.floor(bar/10)):
            print(self.U,end = "")
        print()
    def changeIcon(self, f, u):
        self.F = f
        self.U = u

    def __init__(self, decimal, t):
        self.total = t
        if platform.system() == 'Windows':
            self.clear = "cls"
        elif platform.system() == 'Darwin' or platform.system() == 'Linux':
            self.clear = "clear"
        else:
            print("system error, can't find correct OS")
        self.D = decimal
