from appJar import gui

app=gui("Grid Demo", "1200x800", useTtk=True)

app.setSticky("news")
app.setExpand("both")
app.setFont(20)

#function for the button
def press(btn):
    print(btn)

#Notebook is used for different tabs such as proximity,feet and familiarisation
app.startNotebook("Notebook")
#start of proximity tab
app.startNote("Proximity")

app.addNamedButton("Absolute","ab1",press,row=0,column=2,rowspan=0,colspan=0)
app.addNamedButton("Relative","rel1",press,row=1,column=2,rowspan=0,colspan=0)
app.addNamedButton("Repeat","rep1",press,row=2,column=0,rowspan=0,colspan=0)
app.addNamedButton("Restore","res1",press,row=2,column=1,rowspan=0,colspan=0)
app.addLabel("                ",row=2,column=2,rowspan=0,colspan=0)
app.addNamedButton("Save","sav1",press,row=2,column=3,rowspan=0,colspan=0)
app.addNamedButton("Next Pattern","nex1",press,row=2,column=4,rowspan=0,colspan=0)

app.stopNote()

#start of Feet tab
app.startNote("Feet")

app.addNamedButton("  Absolute  ","ab2",press,row=0,column=2,rowspan=0,colspan=0)
app.addNamedButton("  Relative  ","rel2",press,row=1,column=2,rowspan=0,colspan=0)
app.addButton("Repeat",press,row=2,column=0,rowspan=0,colspan=0)
app.addButton("Restore",press,row=2,column=1,rowspan=0,colspan=0)
app.addLabel("               ",row=2,column=2,rowspan=0,colspan=0)
app.addButton("Save",press,row=2,column=3,rowspan=0,colspan=0)
app.addButton("Next Pattern",press,row=2,column=4,rowspan=0,colspan=0)
app.stopNote()

#start of Familiarisation tab
app.startNote("Familiarisation")

app.addNamedButton("  Proximity  ","pr2",press,row=0,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Intimate",row=1,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Personal",row=2,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Social",row=3,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity", "Public",row=4,column=2,rowspan=0,colspan=0)
app.addRadioButton("proximity", "General Public",row=5,column=2,rowspan=0,colspan=0)

app.addNamedButton("  Feet  ","feet2",press,row=0,column=4,rowspan=0,colspan=0)
app.addRadioButton("feet", "5",row=1,column=4,rowspan=0,colspan=0)
app.addRadioButton("feet", "10",row=2,column=4,rowspan=0,colspan=0)
app.addRadioButton("feet", "15",row=3,column=4,rowspan=0,colspan=0)
app.addRadioButton("feet", "20",row=4,column=4,rowspan=0,colspan=0)
app.addRadioButton("feet", "25",row=5,column=4,rowspan=0,colspan=0)
app.stopNote()

app.stopNotebook()

app.go()
