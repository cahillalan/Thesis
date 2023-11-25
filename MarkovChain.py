import random
import numpy

def chooseState(myprobs):

    states = [1,2,3,4]
    state = numpy.random.choice(states,p = myprobs)

    return state

def calculateprob(size,state,mortalityrate):



## sets the values for the contiguous values
    c = []
    for i in range(4):
        t = i + 1
        if (t + 1) == state:
            c.append(1)
        elif (t - 1) == state:
            c.append(1)
        else: c.append(.5)
## higher states, for higher states 1 = mortality rate, for lower states size* .5
    h = []
    for i in range(4):
        if (i+1) > state:
            h.append(1+mortalityrate)
        else:
            h.append(.5)
## calculates the probabilities by multiplying h *c
    myprobs = []
    for i in range(4):
        prob = h[i]*c[i]
        myprobs.append(prob)
    probs =[]
    ## apply the third principle
    if state == 4:
        probs = [0,0,0,1]
    else:
        ##standardise the probabilities.
        for i in myprobs:
            probs.append(i/sum(myprobs))

    return probs
def hiddenstates(size,state,newstate):
    if newstate == 4 and state == 3:
        a = [3,4]
        p = [.1,.9]
        newstate = numpy.random.choice(a, p = p)
    elif newstate == 3 and state == 1:
        a =[1,3]
        p = [.1,.9]
        newstate = numpy.random.choice(a, p=p)
    elif newstate == 2 and state == 1:
        a =[1,2]
        p =[.2,.8]
        newstate = numpy.random.choice(a, p=p)
    elif newstate == 4 and state == 2:
        a = [2,4]
        p=[.1,.9]
        newstate = numpy.random.choice(a, p=p)
    elif newstate == 4 and state == 1:
        a = [1,4]
        p = [.3,.7]
        newstate = numpy.random.choice(a, p=p)

    return newstate

def setState(size,state,mortalityrate):
    myprobs = calculateprob(size,state,mortalityrate)
    newstate = chooseState(myprobs)
    newstate = hiddenstates(size,state,newstate)
    #print('start')
    #print(state)
    #print(myprobs)
    #print(newstate)
    #print('markov')

    return newstate
