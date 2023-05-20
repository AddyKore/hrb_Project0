'''
FunctionCyclePlan uses the period we set in self.plan.setPeriod(period) and creates a phase, this phase is then sent to the function noted next
'''

from joy import JoyApp
from joy.misc import curry
from joy.decl import *
from math import sin,pi
from joy.plans import FunctionCyclePlan
from joy.plans import Plan


class moveForward( Plan ):
    def __init__(self,*arg,**kw):
        Plan.__init__(self, *arg, **kw)
        self.upper = self.app.upper
        self.lower = self.app.lower
        self.s = self.app.s
        self.plan = self.app.plan

    def onStart( self ):
        pass
        #progress("Starting driving")

    def onStop ( self ):
        pass
        #progress("Stopping driving")    
    
    def behavior(self):
        yield
        self.lower.set_pos(0)
        self.s = self.app.s
        self.plan.start()
        yield
        progress(self.s*9000)
        self.upper.set_pos(self.s*9000)
        yield  



        #self.upper.set_speed(self.speed)
        #self.lower.set_speed(self.speed)

        #self.upper.set_pos(umaxPos)   # motors need time to process the movement before we can send them next move
        #yield 15/self.speed
        #self.upper.set_pos(uminPos)
        #yield 15/self.speed

        #so if there is while loop it is stuck in there
        #is it is simple set pos then delay is needed
        

class turnL( Plan ):
    def __init__(self,*arg,**kw):
        Plan.__init__(self, *arg, **kw)
        self.upper = self.app.upper
        self.lower = self.app.lower
        self.s = self.app.s
        self.plan = self.app.plan

    def onStart( self ):
        progress("Starting driving")

    def onStop ( self ):
        progress("Stopping driving")
    
    def behavior(self):
        yield        
        self.s = self.app.s
        self.plan.start()
        yield
        progress(self.s*7000)
        self.upper.set_pos(self.s*7000)
        if(self.s<0.1):
            self.lower.set_pos(self.s*4500)
        yield  

class turnR( Plan ):
    def __init__(self,*arg,**kw):
        Plan.__init__(self, *arg, **kw)
        self.upper = self.app.upper
        self.lower = self.app.lower
        self.s = self.app.s
        self.plan = self.app.plan

    def onStart( self ):
        progress("Starting driving")

    def onStop ( self ):
        progress("Stopping driving")
    
    def behavior(self):
        yield        
        self.s = self.app.s
        self.plan.start()
        yield
        progress(self.s*7000)
        self.upper.set_pos(self.s*7000)
        if(self.s<0.1):
            self.lower.set_pos(self.s*4500*-1)
        yield  
       


class botControlFC(JoyApp):
    def __init__(self,upper,lower,*arg,**kw):
        JoyApp.__init__(self, *arg,**kw)
        self.upper = getattr(self.robot.at, upper)
        self.lower = getattr(self.robot.at, lower)
        self.period = 1
        self.s=0
    

    def fun(self, phase):
        self.s=  sin(phase*2*pi)

    def onStart(self):
        self.plan = FunctionCyclePlan(self, self.fun, 24)
        self.plan.setPeriod(self.period)
        self.moveForward = moveForward(self)
        self.turnR = turnR(self)
        self.turnL = turnL(self)
        progress("Initializing...")
        #self.moveForward.start()

    def onEvent(self,evt):
        if evt.type == KEYDOWN:
            if evt.key == K_1:
                self.period = 3
                self.plan.setPeriod(self.period)

            if evt.key == K_2:
                self.period = 2.5
                self.plan.setPeriod(self.period)

            if evt.key == K_3:
                self.period = 2
                self.plan.setPeriod(self.period)

            if evt.key == K_4:
                self.period = 1.5
                self.plan.setPeriod(self.period)
            
            if evt.key == K_UP and not self.moveForward.isRunning():
                self.moveForward.start()

            elif evt.key == K_RIGHT and not self.turnR.isRunning():
                self.turnR.start()

            elif evt.key == K_LEFT and not self.turnL.isRunning():
                self.turnL.start()
            
            else:
                return JoyApp.onEvent(self,evt)
        
        if evt.type == KEYUP:
            if evt.key == K_UP:
                self.plan.stop()

    


if __name__ == "__main__":
    from sys import argv, stdout, exit

    robot = None          #setting variables for robot module count and module address
    upper = "#upper"
    lower = "#lower"

    args = list(argv[1:])

    while args:
        arg = args.pop(0)
        if arg=='--mod-count' or arg == '-c':
            #detects number of modules specified after -c
            N = int(args.pop(0))
            robot = dict(count=N)

        elif arg==' --upper' or arg=='-u':
            #detects the address of the upper module
            upper = args.pop(0)

        elif arg==' --lower' or arg=='-l':
            #detects the address of the lower module
            lower = args.pop(0)

        elif arg=='--help' or arg == '-h':
            #help prompt
            stdout.write(""" """%argv[0])
            exit(1)

    # ENDS cmdline parsing loop
  #start an interface

    app = botControlFC(upper,lower,robot=robot)
    app.run()
    
