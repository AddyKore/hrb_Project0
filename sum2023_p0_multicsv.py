assert __name__=="__main__"

from joy.decl import *
from joy.multicsv import MultiCSVApp

class DemoApp( MultiCSVApp ):
    onKey_w = 'tryinglast.csv'
    onKey_a = 'turnRR.csv'
    onKey_s = 'turnRR.csv'
    onKey_d = 'turnL.csv'

    def onStart(self):
        MultiCSVApp.onStart(self)
        # add your onStart() code here

    def onEvent(self,evt):
        # Handle any events you want to handle here and return
        # then leave the rest to the superclass
        return MultiCSVApp.onEvent(self,evt)
    
from ckbot.logical import DiscoveryError
try:
    app = DemoApp(robot=dict(count=2))
except DiscoveryError:
    print(">>>> Could not find physical modules; using simulated ones instead")

    from ckbot import nobus
    from ckbot.ckmodule import  DebugModule
    nids = [5,6,7]
    for nid in nids:
        nobus.NID_CLASS[nid]=DebugModule
    app = DemoApp( robot=dict( arch=nobus, fillMissing=True, required=nids, timeout=0.01 ))

app.run()
