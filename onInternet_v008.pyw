import wx
import urllib2
import time
import wx
import urllib2
import time
import os, re, subprocess, threading

TRAY_TOOLTIP = 'Internet'
TRAY_ICON = 'C:\\Users\\sped\\Desktop\\newFolder\\test.png'

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item

class TaskBarIcon(wx.TaskBarIcon):
    def __init__(self):
        super(TaskBarIcon, self).__init__()
        self.pingGoogle()
        
    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self):
        icon = wx.IconFromBitmap(wx.Bitmap('C:/Users/sped/Documents/GitHub/onInternet/icons/slow.png'))
        self.SetIcon(icon, TRAY_TOOLTIP)
        
    def pingGoogle(self):
        threading.Timer(5.0, self.pingGoogle).start()
        try:
            myPing = int(self.getPing()) 
            self.set_icon()
            if myPing<50:
                print myPing
                path = 'C:/Users/sped/Documents/GitHub/onInternet/icons/fast.png'
                icon = wx.IconFromBitmap(wx.Bitmap(path))
                self.SetIcon(icon, TRAY_TOOLTIP)

            if myPing>50 and myPing<200:
                print myPing
                path = 'C:/Users/sped/Documents/GitHub/onInternet/icons/medium.png'
                icon = wx.IconFromBitmap(wx.Bitmap(path))
                self.SetIcon(icon, TRAY_TOOLTIP)

            if myPing>200:
                print myPing
                path = 'C:/Users/sped/Documents/GitHub/onInternet/icons/slow.png'
                icon = wx.IconFromBitmap(wx.Bitmap(path))
                self.SetIcon(icon, TRAY_TOOLTIP)
            return path
        except:
            path = 'C:/Users/sped/Documents/GitHub/onInternet/icons/no.png'
            icon = wx.IconFromBitmap(wx.Bitmap(path))
            self.SetIcon(icon, TRAY_TOOLTIP)

    
    def getPing(self):
        pingTime = subprocess.check_output('ping www.google.com -n 1', shell=True)

        try:
            asdf=re.search(r'(?:time=)(\d*)', pingTime) # matchesd
            myNumber=asdf.group(0).strip('time=')
        except:
            pass    
        pass
        return myNumber
   
    def on_exit(self, event):   
        wx.CallAfter(self.Destroy)
  

def main():
    app = wx.PySimpleApp()
    TaskBarIcon()
    app.MainLoop()



if __name__ == '__main__':
    main()