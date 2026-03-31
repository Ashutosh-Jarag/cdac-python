import time
def checkExecutionTime(func):
    def inner():
        start = time.time()
        func()
        end=time.time()
        print("Time required for execution is: ",end-start)
    return inner


@checkExecutionTime
def printSqr():
    for i in range(1,1000):
        print(i*i)

printSqr()

printSqr()