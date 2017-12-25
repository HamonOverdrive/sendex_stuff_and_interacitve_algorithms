from pythonds.basic.queue import Queue

import random

# tracks if printer has current task or not
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    # tick method decrements the internal timer and sets the printer to idle if the task is completed.
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

# represents 1 printing task
# This timestamp will represent the time that the task was created and placed in the printer queue.
# The waitTime method can then be used to retrieve the amount of time spent in the queue before printing begins.
class Task:
    def __init__(self,time):
        self.timestamp = time
        # if there are double the students from 20 students pages jump from 20 to 40 print tasks per hour
        self.pages = random.randrange(1,41)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

# if 40 students 1 task every 90 seconds on average
def newPrintTask():
    num = random.randrange(1,91)
    if num == 90:
        return True
    else:
        return False

# run 10 independent trials
for i in range(10):
    # 3600 represents seconds of 60 minutes
    simulation(3600,10)

# to parametertize number of students make a function that uses input for the amount of student which changes the print task amount
# and the amount of rand in class self.pages
