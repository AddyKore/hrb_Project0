from joy import JoyApp
from joy.decl import *
from joy.plans import Plan

maxPos = 7500
minPos = -4500
umidPos = 1500
lmidPos = 0000
corRight = 1000


class moveForward2( Plan ):
  def __init__(self,*arg,**kw):
    Plan.__init__(self, *arg, **kw)
    self.fwdStep = self.app.fwdStep
    self.upper = self.app.upper
  
  def onStart( self ):
    progress("Starting driving")

  def onStop ( self ):
    progress("Stopping driving")

  def behavior(self):
    yield

    cur_pos_u= self.upper.get_pos()
    
    while (cur_pos_u+self.fwdStep< maxPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u + self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(maxPos)

    cur_pos_u = self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> minPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u - self.fwdStep
      self.upper.set_pos(new_pos_u)

    self.upper.set_pos(minPos)

class turnL( Plan ):
  def __init__(self,*arg,**kw):
    Plan.__init__(self, *arg, **kw)
    self.fwdStep = self.app.fwdStep
    self.turnStep = self.app.turnStep
    self.maxRight = self.app.maxRight
    self.maxLeft = self.app.maxLeft
    self.upper = self.app.upper
    self.lower = self.app.lower
  
  def onStart( self ):
    progress("Starting driving")

  def onStop ( self ):
    progress("Stopping driving")

  def behavior(self):
    yield

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> minPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u - self.fwdStep
      self.upper.set_pos(new_pos_u)

    self.upper.set_pos(minPos)

   

    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep> self.maxLeft):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l - self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(self.maxLeft)

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep< umidPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u +  self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(umidPos)


    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep< lmidPos):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l + self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(lmidPos)

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep< maxPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u + self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(maxPos)





class moveForward( Plan ):
  def __init__(self,*arg,**kw):
    Plan.__init__(self, *arg, **kw)
    self.fwdStep = self.app.fwdStep
    self.turnStep = self.app.turnStep
    self.maxRight = self.app.maxRight
    self.maxLeft = self.app.maxLeft
    self.upper = self.app.upper
    self.lower = self.app.lower
  
  def onStart( self ):
    progress("Starting driving")

  def onStop ( self ):
    progress("Stopping driving")

  def behavior(self):
    yield

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep< maxPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u + self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(maxPos)



    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep< lmidPos):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l + self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(lmidPos)

    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep> lmidPos):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l - self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(lmidPos)

    '''
    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> umidPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u -  self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(umidPos)

    
    
    '''
    cur_pos_u = self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> minPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u - self.fwdStep
      self.upper.set_pos(new_pos_u)

    self.upper.set_pos(minPos)



class turnR( Plan ):
  def __init__(self,*arg,**kw):
    Plan.__init__(self, *arg, **kw)
    self.fwdStep = self.app.fwdStep
    self.turnStep = self.app.turnStep
    self.maxRight = self.app.maxRight
    self.maxLeft = self.app.maxLeft
    self.upper = self.app.upper
    self.lower = self.app.lower
  
  def onStart( self ):
    progress("Starting driving")

  def onStop ( self ):
    progress("Stopping driving")

  def behavior(self):
    yield

    cur_pos_u= self.upper.get_pos()

    cur_pos_u = self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> minPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u - self.fwdStep
      self.upper.set_pos(new_pos_u)

    self.upper.set_pos(minPos)


    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep< self.maxRight):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l + self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(self.maxRight)

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep< umidPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u +  self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(umidPos)

    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep> lmidPos):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l - self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(lmidPos)
    
    while (cur_pos_u+self.fwdStep< maxPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u + self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(maxPos)





class botControl( JoyApp ):
  def __init__(self,upper,lower,*arg,**kw):
    JoyApp.__init__(self, *arg,**kw)
    
    self.upper = getattr(self.robot.at, upper)
    self.lower =  getattr(self.robot.at, lower)

    self.fwdStep = 1000
    self.turnStep = 1000
    self.maxRight = 4000
    self.maxLeft = -4000

  def onStart(self):
    self.move = moveForward(self)
    self.turnR = turnR(self)
    self.turnL = turnL(self)
    progress("Initializing...")

  def onEvent(self,evt):
    if evt.type != KEYDOWN:
      return
    # assertion: must be a KEYDOWN event

    if evt.key == K_1:
      self.fwdStep= 250
      self.turnStep= 250
    
    elif evt.key == K_2:
      self.fwdStep= 500
      self.turnStep= 500

    elif evt.key == K_3:
      self.fwdStep= 750
      self.turnStep= 750
  
    elif evt.key == K_4:
      self.fwdStep= 1000
      self.turnStep= 1000

    elif evt.key == K_5:
      self.fwdStep= 1250
      self.turnStep= 1250

    elif evt.key == K_6:
      self.maxLeft = -1000
      self.maxRight = 1000

    elif evt.key == K_7:
      self.maxLeft = -2000
      self.maxRight = 2000

    elif evt.key == K_8:
      self.maxLeft = -3000
      self.maxRight = 3000

    elif evt.key == K_9:
      self.maxLeft = -4000
      self.maxRight = 4000

    if evt.type == KEYDOWN and (evt.key == K_1 or evt.key == K_2 or evt.key == K_3 or evt.key == K_4 or evt.key == K_5 or evt.key == K_6 or evt.key == K_7 or evt.key == K_8 or evt.key == K_9):
      self.move = moveForward(self)
      self.turnR = turnR(self)
      self.turnL = turnL(self)
      progress("Reinitializing...")


    if evt.key == K_UP and not self.move.isRunning():
      self.move.start()

    elif evt.key == K_RIGHT and not self.turnR.isRunning():
      self.turnR.start()

    elif evt.key == K_LEFT and not self.turnL.isRunning():
      self.turnL.start()
    
    else:
      return JoyApp.onEvent(self,evt)



if __name__=="__main__":
  from sys import argv, stdout, exit

  robot = None
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
      stdout.write(""" 
      Usage: %s [options]

    This program controls forward movement as well as steering for a robot developed with 2 motors


      """%argv[0])
      exit(1)

    # ENDS cmdline parsing loop
  #start an interface

  app = botControl(upper,lower,robot=robot)
  app.run()
