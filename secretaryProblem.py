# created when trying to argue about secretary problem.
import random

HEIGHT = 100

def getfloors():
    temp = list(range(HEIGHT))
    random.shuffle(temp)
    return temp

def strategySatisfyAt(floors,satisgyPoint):
    priorMax = max(floors[:satisgyPoint])
    for i in floors[satisgyPoint:]:
        if i > priorMax:
            return i
    return floors[-1]

strategy37 = lambda floors: strategySatisfyAt(floors,37)

def strategyUniform(floors):
    return random.choice(floors)

def tryStrategy(S,times):
    return sum(S(getfloors()) for i in range(times))/float(times)

def main():
    print tryStrategy(strategyUniform,10000)
    print tryStrategy(strategy37,10000)

if __name__ == '__main__':
    main()
