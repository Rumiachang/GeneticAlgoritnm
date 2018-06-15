import numpy as np
import math
HALF_STRING = 8
MAX_STRING = 2*HALF_STRING
MAX_STEP = 50
MAX_POP = 500
class Individual:
    def __init__(self, chrom, fitness):
        self.chrom[MAX_STRING] = chrom[MAX_STRING]
        self.fitness = fitness
    def getChrom(self):
        return self.chrom[MAX_STRING]
    def getFitness(self):
        return self.fitness

chromSize
nPop, nGen
Pm, Pc
funcSeed = 1
Table2ConvBinCode2DecimalNumber = [1,2,4,8,16,32,64,128,256,512]
biasY, normF
kindOfHill = 0
gen, minStep
sumFitness
bestChrom[MAX_STRING]
maxFitness, minFitness, avgFitness, bestFitness
maxIndiv
normD

MAX_BREAK = 20
M_PEAKS = 30

def main():
