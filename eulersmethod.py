
def eulers(nIterations, xCoord, yCoord, approxAt):
    '''
    f(xCoord) = yCoord
    approximate at f(approxAt)
    nIterations is the number of iterations to run
    '''
    x = []
    y = []
    dydx = []
    dy = []
    deltaX = (approxAt - xCoord) / nIterations
    
    
    x.append(xCoord)
    y.append(yCoord)
    
    for i in range(nIterations):

        dydxEquation = x[-1] + y[-1] #dydx = x + y

        dydx.append(dydxEquation)
        dy.append(dydx[-1] * deltaX)
        x.append(x[-1] + deltaX)
        y.append(y[-1] +dy[-1])



    

    return y[-1]



print(eulers(int(input("How many iterations")),float(input("Given x value =   ")), float(input("Given y value =     ")), float(input("Approxiamte f(x) at what x?  "))))