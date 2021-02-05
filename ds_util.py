from math import ceil, floor, sqrt, pow
from sys import argv
import statistics

# stands for data statistics
# INPUT: data file path, data being separated by \newline
class DS:
    # just linear data
    data = []
    def __init__(self, fil):
        with open(fil, 'r') as infil:
            self.data = infil.read().strip().split("\n")
            # convert to float
            self.data = [float(x) for x in self.data]
            self.data.sort()
            
    def mean(self):
        return sum(self.data) / len(self.data)
        
    def variance(self):
        mean = self.mean()
        res = 0
        for x in self.data:
            res = res + (mean - x) * (mean - x)
        return res / (len(self.data) - 1)
        
    def stdev(self):
        return sqrt(self.variance())
        
    def median(self):
        length = len(self.data) - 1
        return (self.data[ceil(length/2)] + self.data[floor(length/2)]) / 2
        
    def py_mean(self):
        return statistics.mean(self.data)
    
    def py_median(self):
        return statistics.median(self.data)
        
    def py_stdev(self):
        return statistics.stdev(self.data)
        
    def print_stat(self):
        print("mean: ", self.mean())
        print("meadian: ", self.median())
        print("standard deviation: ", self.stdev())
        
        print("py mean: ", self.py_mean())
        print("py meadian: ", self.py_median())
        print("py standard deviation: ", self.py_stdev())
        
class DS_Grouped:
    # just linear data
    data = []
    def __init__(self, fil):
        with open(fil, 'r') as infil:
            self.data = infil.read().strip().split("\n")
            # convert to float
            self.data = [[float(x.split(' ')[0]),float(x.split(' ')[1])] for x in self.data]
            
    def count(self):
        res = 0
        for x in self.data:
            res = res + x[1]
        return res
    
    def mean(self):
        res = 0
        count = 0
        for x in self.data:
            res = res + x[0] * x[1]
            count = count + x[1]
        return res/count
        
    def variance(self):
        mean = self.mean()
        res = 0
        for x in self.data:
            res = res + x[0]*x[0]*x[1]
        count = self.count()
        res = res - pow(self.mean() * count, 2)/count
        return res / (count - 1)
        
    def stdev(self):
        return sqrt(self.variance())
        
    def print_stat(self):
        print("mean: ", self.mean())
        print("variance: ", self.variance())
        print("standard deviation: ", self.stdev())
        print("coefficient of variation: ", self.stdev()/self.mean())

if __name__ == "__main__":
    if(len(argv) > 1):
        ds = DS(argv[1])
        ds.print_stat();