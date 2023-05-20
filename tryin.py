from joy import JoyApp
from joy.decl import *
from joy.plans import Plan
import time

umaxPos = 7000
uminPos = -4500
umidPos = 1500
rightPos= 4500
leftPos=4500
lmidPos = 0000

speed = 1

class moveForward( Plan ):
    def __init__(self,*arg,**kw):
        Plan.__init__(self, *arg, **kw)
        self.upper = self.app.upper
        self.lower = self.app.lower

    def onStart( self ):
        progress("Starting driving")

    def onStop ( self ):
        progress("Stopping driving")
    
    def behavior(self):
        yield
        self.upper.set_pos(umaxPos)
        yield 0.5
        self.upper.set_pos(uminPos)
        yield 0.5

        #so if there is while loop it is stuck in there
        #is it is simple set pos then delay is needed
        


class turnL( Plan ):
    def __init__(self,*arg,**kw):
        Plan.__init__(self, *arg, **kw)
        self.upper = self.app.upper
        self.lower = self.app.lower

    def onStart( self ):
        progress("Starting driving")

    def onStop ( self ):
        progress("Stopping driving")
    
    def behavior(self):
        yield

        #self.upper.set_speed(speed)
        #self.lower.set_speed(speed)

        self.upper.set_pos(umaxPos)
        yield 0.5
        self.lower.set_pos(leftPos)
        yield 0.5

        self.upper.set_pos(umidPos)
        yield 0.5
        self.lower.set_pos(lmidPos)
        yield 0.5
        self.upper.set_pos(uminPos)
        yield 0.5

class turnR( Plan ):
    def __init__(self,*arg,**kw):
        Plan.__init__(self, *arg, **kw)
        self.upper = self.app.upper
        self.lower = self.app.lower

    def onStart( self ):
        progress("Starting driving")

    def onStop ( self ):
        progress("Stopping driving")
    
    def behavior(self):
        yield

        self.upper.set_speed(speed)
        self.lower.set_speed(speed)

        self.upper.set_pos(umaxPos)
        yield 0.5
        self.lower.set_pos(rightPos)
        yield 0.5

        self.upper.set_pos(umidPos)
        yield 0.5
        self.lower.set_pos(lmidPos)
        yield 0.5
        self.upper.set_pos(uminPos)
        yield 0.5


class botControl(JoyApp):
    def __init__(self,upper,lower,*arg,**kw):
        JoyApp.__init__(self, *arg,**kw)
        self.upper = getattr(self.robot.at, upper)
        self.lower = getattr(self.robot.at, lower)
    
    def onStart(self):
        self.moveForward = moveForward(self)
        self.turnR = turnR(self)
        self.turnL = turnL(self)
        progress("Initializing...")
        #self.moveForward.start()

    

    def onEvent(self,evt):
        if evt.type != KEYDOWN:
            return
        # assertion: must be a KEYDOWN event

        if evt.key == K_UP and not self.moveForward.isRunning():
            self.moveForward.start()

        elif evt.key == K_RIGHT and not self.turnR.isRunning():
            self.turnR.start()

        elif evt.key == K_LEFT and not self.turnL.isRunning():
            self.turnL.start()
        
        else:
            return JoyApp.onEvent(self,evt)

    

    


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

    app = botControl(upper,lower,robot=robot)
    app.run()
    