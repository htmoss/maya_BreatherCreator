#BREATHER CREATOR

import maya.cmds as mc

#prevents window from being duplicated
if mc.window("breCrtr", ex=True):
    mc.deleteUI("breCrtr", window=True)
    
mc.window("breCrtr", title="BREATHER CREATOR TOOL", s=True, wh=(800, 300))
mc.columnLayout(adj=True)
mc.text(l="Instructions: ")
mc.text(l="1. Select chest on rig and go to Modify -> Add Attribute")
mc.text(l="2. Make one expression called 'Breathing Control' and one called 'Breath Speed'")
mc.text(l="3. Select on the mesh the vertices you want to move while breathing")
mc.text(l="4. Make a flare on the vertices: Animation->Deform->Nonlinear->Flare\n")

mc.text(l="Input name of Flare's Curve channel below")
flareTextbox = mc.textField( w = 50, h = 30)

mc.text(l="Input name of Chest's Breathing Speed channel below")
brSpeedTextbox = mc.textField( w = 50, h = 30)

mc.button(l="Create Breather Effect", w=100, h=100, c="makeBreath()")

mc.showWindow("breCrtr")


def makeBreath():
    flareText = cmds.textField(flareTextbox, query=True, text=True)
    brSpeedText = cmds.textField(brSpeedTextbox, query=True, text=True)
    mc.expression(n = "Auto_Breathing_expr", s = "flareText = (sin(time * brSpeedText))/20", ae=True)
    
