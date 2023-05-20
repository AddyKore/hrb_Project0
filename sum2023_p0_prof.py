from joy import JoyApp
from joy.decl import *
from joy.plans import Plan

umaxPos = 7500
uminPos = -4500
umidPos = 1500
lmaxPos= 4500
lminPos=4500
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
    while (cur_pos_u+self.fwdStep< maxPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u + self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(maxPos)

   

    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep> self.maxLeft):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l - self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(self.maxLeft)

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> umidPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u -  self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(umidPos)


    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep< lmidPos):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l + self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(lmidPos)

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> minPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u - self.fwdStep
      self.upper.set_pos(new_pos_u)

    self.upper.set_pos(minPos)



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
    fwdStep = self.app.fwdStep
    turnStep = self.app.turnStep
    maxRight = self.app.maxRight
    maxLeft = self.app.maxLeft
    upper = self.app.upper
    lower = self.app.lower
  
    cur_pos_u= upper.get_pos()
    while (cur_pos_u+fwdStep< maxPos):
      fwdStep = self.app.fwdStep
      upper = self.app.upper
      cur_pos_u= upper.get_pos()
      yield 0.05
      new_pos_u = cur_pos_u + fwdStep
      upper.set_pos(new_pos_u)
    
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
    while (cur_pos_u+self.fwdStep< maxPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u + self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(maxPos)



    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep< self.maxRight):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l + self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(self.maxRight)

    cur_pos_u= self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> umidPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u -  self.fwdStep
      self.upper.set_pos(new_pos_u)
    
    self.upper.set_pos(umidPos)

    cur_pos_l = self.lower.get_pos()
    while (cur_pos_l+self.turnStep> lmidPos):
      cur_pos_l = self.lower.get_pos()
      new_pos_l = cur_pos_l - self.turnStep
      self.lower.set_pos(new_pos_l)
    
    self.lower.set_pos(lmidPos)
    

    cur_pos_u = self.upper.get_pos()
    while (cur_pos_u+self.fwdStep> minPos):
      cur_pos_u= self.upper.get_pos()
      new_pos_u = cur_pos_u - self.fwdStep
      self.upper.set_pos(new_pos_u)

    self.upper.set_pos(minPos)



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

  # def onEvent(self,evt):
  #   if evt.type != KEYDOWN:
  #     return
  #   # assertion: must be a KEYDOWN event

  def on_K_1(self,evt):
    self.fwdStep= 250
    self.turnStep= 250
    
  def on_K_2(self,evt):
      self.fwdStep= 500
      self.turnStep= 500

  def on_K_3(self,evt):
      self.fwdStep= 750
      self.turnStep= 750
  
  def on_K_4(self,evt):
      self.fwdStep= 1000
      self.turnStep= 1000

  def on_K_5(self,evt):
      self.fwdStep= 1250
      self.turnStep= 1250

  def on_K_6(self,evt):
      self.maxLeft = -1000
      self.maxRight = 1000

  def on_K_7(self,evt):
      self.maxLeft = -2000
      self.maxRight = 2000

  def on_K_8(self,evt):
      self.maxLeft = -3000
      self.maxRight = 3000

  def on_K_9(self,evt):
      self.maxLeft = -4000
      self.maxRight = 4000
 
    if evt.type == KEYDOWN and evt.key in {K_1,K_2,K_3,K_4,K_5,K_6,K_7,K_8,K_9}
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

    The keys used to control the robot are:
      'up-arrow' -- move forwards - one press is one forwards cycle
      '1', '2', '3', '4' or '5' -- sets arm speed as follows 250, 500, 750, 1000, 1250 ; default = 1000.
      '6', '7', '8' or '9' -- sets steering angle as follows 10, 20, 30,40 : default 40.
      'f' -- move front motor individually one cycle
      'a' -- steer left - turns robot left
      'd' -- steer right - turn robot right
      'left-arrow' -- turns the robot left and moves forwards (maintains a left turn when held)
      'right-arrow' -- turns the robot right and moves forwards (maintains a right turn when held) 
      'r' -- reset the robot to ready position (straightened out)
      'c' -- sets the robot to compact starting position (fits within 20cm x 20cm)
      'q' -- saves the turn angle to turn left or turn right plans
      'escape' -- exit program

    Command Line Options:
      --mod-count <number> | -c <number>
        Search for specified number of modules at startup

      --front <motor | -f <motor>
      --middle <motor> | -m <motor>
      --back <motor> | -b <motor>
        Specify the motors used for moving and steering

        Ex command:
        $  python3 doubleGorilla.py -c 3 -f Nx0C -m Nx15 -b Nx97

        NOTE: to use robot modules you MUST specify a -c option

    Note* Code designed for motors in the following configuration:
    * Front and back motors pivot in the direction of travel = positive dynamixel angle
    * Middle motor pivot right = negative dynamixel angle

      """%argv[0])
      exit(1)

    # ENDS cmdline parsing loop
  #start an interface

  app = botControl(upper,lower,robot=robot)
  app.run()
