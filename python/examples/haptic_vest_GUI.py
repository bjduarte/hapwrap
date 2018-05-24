#!/usr/bin/python3

import wx   

class Haptic_Vest(wx.Frame): 
            
   def __init__(self, parent, title): 
      super(Haptic_Vest, self).__init__(parent, title = title,size = (300,200)) 

      self.InitUI() 
   def InitUI(self):    
      pnl = wx.Panel(self)

      # self.person = wx.RadioButton(pnl, 11, label = 'person',
      #    pos = (10,10), style = wx.RB_GROUP)
      # self.vehicle = wx.RadioButton(pnl,22, label = 'vehicle',pos = (10,40))
      # self.chair = wx.RadioButton(pnl,33, label = 'chair',pos = (10,70))
      # self.Bind(wx.EVT_RADIOBUTTON, self.OnRadiogroup)

      elevationList = ['person', 'vehicle', 'chair']
      distanceList = ['distance_10', 'distance_15', 'distance_20', 'distance_25'] 
      directionList = ['0 degrees', '45 degrees', '90 degrees', '135 degrees', '180 degrees', '225 degrees', '270 degrees', '315 degrees']

      self.elevationBox = wx.RadioBox(pnl, label = 'ElevationRadioBox', choices = elevationList,
         majorDimension = 1, style = wx.RA_SPECIFY_COLS) 
      self.elevationBox.Bind(wx.EVT_RADIOBOX, self.onElevationRadioBox) 


      self.distanceBox = wx.RadioBox(pnl, label = 'DistanceRadioBox', choices = distanceList,
         majorDimension = 1, style = wx.RA_SPECIFY_COLS) 
      self.distanceBox.Bind(wx.EVT_RADIOBOX, self.onDistanceRadioBox) 

      self.directionBox = wx.RadioBox(pnl, label = 'directionRadioBox', choices = directionList,
         majorDimension = 1, style = wx.RA_SPECIFY_COLS) 
      self.directionBox.Bind(wx.EVT_RADIOBOX, self.onDirectionRadioBox) 

      sizer = wx.GridBagSizer(hgap = 5, vgap = 5)
      sizer.Add(self.elevationBox, pos = wxALIGN_LEFT)
      sizer.Add(self.distanceBox, pos = wx.DEFAULT_POS)
      sizer.Add(self.directionBox, pos = wx.DEFAULT_POS)


      self.Centre()
      self.Show(True)

   def onElevationRadioBox(self, e): 
      print(self.elevationBox.GetStringSelection(),' is at index ',self.elevationBox.GetSelection())
      ele = self.elevationBox.GetSelection()

   def onDistanceRadioBox(self,e): 
      print(self.distanceBox.GetStringSelection(),' is at index ',self.distanceBox.GetSelection())
      dist = self.distanceBox.GetSelection()

   def onDirectionRadioBox(self, e):
     print(self.directionRadioBox.GetStringSelection(), self.directionRadioBox.GetSelection())

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = Haptic_Vest(None, 'Elevation and Distance')
    frame.Show()

    app.MainLoop()
