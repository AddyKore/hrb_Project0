from joy import JoyApp
from joy.misc import curry
from joy.decl import *
from math import sin,pi
from joy.plans import GaitCyclePlan
from joy.plans import Plan
from joy.misc import loadCSV


class botControlFC(JoyApp):

    moveFwd = loadCSV("movefwd.csv")
    def __init__(self,upper,lower,*arg,**kw):
        JoyApp.__init__(self, *arg,**kw)
   

    def onStart(self):
        if self.robot is not None:
            #self.planfwd = GaitCyclePlan( self, self.moveFwd, maxFreq = 0.3, Nx10='Nx10/@set_pos', Nx04='Nx04/@set_pos')
            #self.planL = GaitCyclePlan( self, self.turnL, maxFreq = 0.3, Nx10='Nx10/@set_pos', Nx04='Nx04/@set_pos')
            self.planR = GaitCyclePlan( self, self.moveFwd, maxFreq = 0.3, Nx10='Nx10/@set_pos', Nx04='Nx04/@set_pos')
        else:
            self.plan = GaitCyclePlan( self, self.moveFwd, maxFreq = 0.3,
            x='#catX', y='#catY')

        self.planR.onStart = curry(progress,">>> START")
        self.planR.onStop = curry(progress,">>> STOP")
        self.planR.setFrequency(0.1)

    def onEvent(self,evt):
        if evt.type == KEYDOWN:
            if evt.key == K_1:
                self.period = 0.3
                #self.planL.setFrequency(self.period)
                self.planR.setFrequency(self.period)
                #self.planfwd.setFrequency(self.period)

            elif evt.key == K_2:
                self.period = 0.6
                #self.planL.setFrequency(self.period)
                self.planR.setFrequency(self.period)
                #self.planfwd.setFrequency(self.period)


            elif evt.key == K_3:
                self.period = 0.9
                #self.planL.setFrequency(self.period)
                self.planR.setFrequency(self.period)
                #self.planfwd.setFrequency(self.period)


            elif evt.key == K_4:
                self.period = 1.2
                #self.planL.setFrequency(self.period)
                self.planR.setFrequency(self.period)
                #self.planfwd.setFrequency(self.period)

            elif evt.key in [K_q,27]: # 'q' and [esc] stop program
                self.stop()

            elif evt.key==K_SPACE: # [space] stops cycles
                #self.planfwd.setPeriod(0)
                #self.planL.setPeriod(0)
                self.planR.setPeriod(0)
                progress('Stopped motion')
        
            elif evt.key == K_UP:
                self.planR.start()

            elif evt.key == K_RIGHT:
                self.planR.start()

            elif evt.key == K_LEFT:
                self.planR.start()
            
            else:
                return JoyApp.onEvent(self,evt)
        
        if evt.type == KEYUP:
            if evt.key == K_UP:
                self.planR.stop()
            elif evt.key == K_RIGHT:
                self.planR.stop()
            elif evt.key == K_LEFT:
                self.planR.stop()
            
            

    


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
    
