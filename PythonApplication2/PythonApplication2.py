import numpy as np
import math
import random
HALF_STRING = 8
MAX_STRING = 2*HALF_STRING
MAX_STEP = 50
MAX_POP = 500
class Individual:
    #chrom=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    def __init__(self, chrom, fitness):
        self.chrom = chrom
        self.fitness = fitness
        print("あああああああ")
    def getChrom(self):
        return self.chrom
    def getFitness(self):
        return self.fitness
    def setFitness(self,fitness):
        self.fitness = fitness
    def setChrom(self, chrom):
        self.chrom = chrom

#oldPop= [Individual([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0)]
#newPop =[Individual([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 0)]


chromSize=MAX_STRING
nPop=MAX_POP
nGen=100
probOfMutation=0.1
probOfCrossOver=0.02
funcSeed = 1
table2ConvBinCode2Dec = [1,2,4,8,16,32,64,128,256,512]
biasY=60
normF=120
kindOfHill = 0

"""
sumFitness=0
bestChrom=[]
maxFitness=0
minFitness=0
avgFitnes=0
bestFitness=0.0
maxIndiv=0
"""

MAX_BREAK = 20
M_PEAKS = 30

def initPopulation(oldPop, newPop):
    i=0
    for i in range(nPop):
       print("うううううう")
       print(str(i))
       oldPop.append(Individual(genChrom(MAX_STRING), 0))
       oldPop[i].setFitness(calcMountHeightFitnessFromChrom(oldPop[i].getChrom()))
       newPop.append(Individual(genChromZeroPadded(MAX_STRING), 0))
       
    return 1


def copyPopulation(oldPop, newPop):
    for i in range(MAX_POP):
        oldPop[i].setChrom(newPop[i].getChrom())
        oldPop[i].setFitness(newPop[i].getFitness())


def selectChrom(pop):
    sum=0.0
    i= 0
    r=random.random()*Statistics(pop).getSumFitness()
    while(True):
        sum= sum + pop[i].getFitness()
        ++i
        if(not(sum < r and i < nPop)): break
    return i-1

def go2NextGeneration(oldPop,newPop):
    i=0
    mate1=0
    mate2=0
    while(True):
        mate1=selectChrom(oldPop)
        mate2=selectChrom(oldPop)
        crossOver(oldPop[mate1].getChrom(), oldPop[mate2].getChrom(),
                 newPop[i].getChrom(), newPop[i+1].getChrom(), MAX_STRING)
        mutation(newPop[i].getChrom(), MAX_STRING)
        mutation(newPop[i+1].getChrom(), MAX_STRING)
        newPop[i].setFitness(calcMountHeightFitnessFromChrom(newPop[i].getChrom()))
        newPop[i+1].setFitness(calcMountHeightFitnessFromChrom(newPop[i+1].getChrom()))
        i= i+2
        if(not(i < nPop)): break


def crossOver(parent1, parent2, child1, child2, chromSize):
    i1=0
    i2=0
    if(flip(probOfCrossOver)):
        i1=math.floor(chromSize*random.random())
        i2=math.floor(chromSize*random.random())
        if(i1 > i2):
            i= i1
            i1=i2
            i2=i
        for i in range(i1):
            child1[i]=parent1[i]
            child2[i]=parent2[i]
        for i in range(i1, i2):
            child2[i]=parent1[i]
            child1[i]=parent2[i]
        for i in range(i2, chromSize):
            child1[i]=parent1[i]
            child2[i]=parent2[i]
    else:
        for i in range(chromSize):
            child1[i]=parent1[i]
            child2[i]=parent2[i]

def mutation(chrom, chromSize):
    if(flip(probOfMutation)):
        i=math.floor(chromSize*random.random())
        chrom[i]=1-chrom[i]


def mountHeightFunc(x,z):
    rd=math.pi/180
    
    wk=math.sqrt(x*x+z*z)*rd
    y=30*(math.cos(wk)+math.cos(3*wk))
    biasY=60.0
    normF=120.0
    return y

def calcMountHeightFitnessFromChrom(chrom):
    x=0
    z=0
    for i in range(HALF_STRING):
        if(chrom[i]):
            x = x+ table2ConvBinCode2Dec[i]
        if(chrom[i+HALF_STRING]):
            z = z + table2ConvBinCode2Dec[i]
    if(x > table2ConvBinCode2Dec[HALF_STRING]):
        x = x - table2ConvBinCode2Dec[HALF_STRING + 1]
    if(z > table2ConvBinCode2Dec[HALF_STRING]):
        z = z - table2ConvBinCode2Dec[HALF_STRING + 1]
    return (mountHeightFunc(x, z) + biasY)/normF

def calcPointXZFromChrom(chrom):
    x=0
    z=0
    Pxz =[0,0]
    for i in range(HALF_STRING):
        if(chrom[i]):
            x = x+ table2ConvBinCode2Dec[i]
        if(chrom[i+HALF_STRING]):
            z = z + table2ConvBinCode2Dec[i]
    if(x > table2ConvBinCode2Dec[HALF_STRING]):
        x = x - table2ConvBinCode2Dec[HALF_STRING + 1]
       
    if(z > table2ConvBinCode2Dec[HALF_STRING]):
        z = z - table2ConvBinCode2Dec[HALF_STRING + 1]
    Pxz[0]=x
    Pxz[1]=z
    return (Pxz)



class Statistics:
    def __init__(self, pop):
        self.pop=pop

    def getSumFitness(self):
        sumFitness = 0.0
        for i in range(nPop):
            sumFitness = sumFitness + self.pop[i].getFitness()
        return (sumFitness)
    def getMaxChrom(self):
        return (self.pop[self.getiMax()].getChrom())

    def getMaxFitness(self):
        return (self.pop[self.getiMax()].getFitness())

    def getiMax(self):
        maxFitness = 0.0
        iMax= 0
        for i in range(nPop):
           if(self.pop[i].getFitness() >= maxFitness):
               maxFitness = self.pop[i].getFitness()
               iMax=i
        return (iMax)
        
    """
    bestChrom= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    iMax=0
    iMin=0
    sumFitness = bestFitness= maxFitness = minFitness=pop[0].getFitness()
    
    for i in range(1, nPop):
        sumFitness = sumFitness + pop[i].getFitness()
        if(pop[i].getFitness() >= maxFitness):
            maxFitness = pop[i].getFitness()
            iMax=i
        if(pop[i].getFitness() < minFitness):
            minFitness = pop[i].getFitness()
            iMin =i
    avgFitness = sumFitness / nPop
    maxIndiv = iMax
    if(bestFitness < maxFitness):
            bestChrom = pop[iMax].getChrom()
            bestFitness = maxFitness
    print(str(gen) + "　　" + str(bestFitness)+"　　"+str(calcPointXZFromChrom(bestChrom)[0])+"　　"+str(calcPointXZFromChrom(bestChrom)[1]))
    """

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

def genChromZeroPadded(chromSize):
    chrom =[]
    for i in range(chromSize):
        chrom.append(0)
    return(chrom)


def genChrom(chromSize):
    #chrom =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
   
 #------------------------------------------------------------------------------------
 #chromSizeの長さの遺伝子（バイナリコード）をランダムに生成する，それのリストchrom[]を返す
 #返り値:chrom[chromSize]
 #------------------------------------------------------------------------------------
    chrom = genChromZeroPadded(chromSize)
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

def main():
    oldPop =[]
    newPop =[]
    
    initPopulation(oldPop, newPop)


    gen = 0
    bestFitness = 0.0
    currentMaxFitness = 0.0
    currentMaxChrom =genChromZeroPadded(chromSize)
    bestChrom=genChromZeroPadded(chromSize)
    #print("サイクルごとの根の値を羅列します．")
    print("gen　　カレント最大フィットネス　　X　　Z")
    print("--------------------------------------------")
    
    cycles = 10
    for gen in range(cycles):
        pxz = [2]
        pxz = calcPointXZFromChrom(currentMaxChrom)
        print(str(gen) + "　　" + str(currentMaxFitness)+"　　"+str(pxz[0])+"　　"+str(pxz[1]))
        if(not(gen < nGen)): break 
        stats = Statistics(oldPop)
        currentMaxFitness = stats.getMaxFitness()
        currentMaxChrom = stats.getMaxChrom()
        if(stats.getMaxFitness() > bestFitness):
            bestFitness = stats.getMaxFitness()
            bestChrom = stats.getMaxChrom()

        go2NextGeneration(oldPop, newPop)
        copyPopulation(oldPop, newPop)
    print("ベストフィットネス："+str(bestFitness))
    print("ベストフィットネスとなる(X,Z)=" + str( calcPointXZFromChrom(bestChrom)))
       # statistic(gen, oldPop)

if __name__ == "__main__":
    main()

