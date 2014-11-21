import wx
import urllib2
import time

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
        
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.on_refresh)
        
        while True:
            self.set_icon()


    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'refresh', self.on_refresh)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self):
        path = self.refresh()
        icon = wx.IconFromBitmap(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)
        time.sleep(6)


    def on_exit(self, event):
        wx.CallAfter(self.Destroy)

    def on_refresh(self, event):
        if self.internet_on() == True:
            TRAY_ICON = 'C:\\Users\\sped\\Desktop\\newFolder\\yes.png'
            self.set_icon(TRAY_ICON)
            print 'internet is on'
        else:
            print 'internet is off'
            TRAY_ICON = 'C:\\Users\\sped\\Desktop\\newFolder\\no.png'
            self.set_icon(TRAY_ICON)

       
    def refresh(self):
        if self.internet_on() == True:
            TRAY_ICON = 'C:\\Users\\sped\\Desktop\\newFolder\\yes.png'
        else:
            TRAY_ICON = 'C:\\Users\\sped\\Desktop\\newFolder\\no.png'
            print 'program started'  
        return TRAY_ICON       


    def internet_on(self):
        try:
            response=urllib2.urlopen('http://74.125.228.100',timeout=1)
            return True
        except urllib2.URLError as err: pass
        return False



def main():
    app = wx.PySimpleApp()
    TaskBarIcon()
    app.MainLoop()



if __name__ == '__main__':
    main()