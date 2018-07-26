import numpy as np
import math
import random
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

oldPop= Individual()
Pxy[2]
chromSize=MAX_STRING
nPop=MAX_POP
nGen=100
Pm=0.1
Pc=0.02
funcSeed = 1
table2ConvBinCode2Dec = [1,2,4,8,16,32,64,128,256,512]
biasY, normF
kindOfHill = 0
gen=0
minStep
sumFitness
bestChrom[MAX_STRING]
maxFitness, minFitness, avgFitness
bestFitness = 0.0
maxIndiv
normD

MAX_BREAK = 20
M_PEAKS = 30

def initPopulation():
    i=0
    while(i < nPop):


def mountHeightFunc(x,z):
    rd=math.pi/180
    y,yy,wk
    wk=math.sqrt(x*x+z*z)*rd
    y=30*(math.cos(wk)+math.cos(3*wk))
    biasY=60.0
    normF=120.0
    return y

def statistic


def flip(prob): 
 #------------------------------------------------------------------------------------
 #0以上1以下の乱数がprobと等しいか小さいときTrue,そうでないときはFalse返す
 #返り値:bool
 #------------------------------------------------------------------------------------
    if(prob == 1.0): 
        return(True)
    elif(random.random() <= prob):
        return(True)
    else:
        return(False)


def genChrom(chromSize):
    chrom=[]
 #------------------------------------------------------------------------------------
 #chromSizeの長さの遺伝子（バイナリコード）をランダムに生成する，それのリストchrom[]を返す
 #返り値:chrom[chromSize]
 #------------------------------------------------------------------------------------
    for i in range(chromSize):
        if(flip(0.5)):
            chrom[i]=1
        else:
            chrom[i]=0
    return(chrom)

def rangeRand(min, max):
    return ((max - min)*random.random()+min)
"""
def random():
    i=rand()
    if (i!=0): --i
    r=i/0x7fff
    return r
"""

def initPop():
    i=0

def main():
