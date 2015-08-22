import wx
import time
import wx.lib.agw.pybusyinfo as PBI

# Display the dialog Box to enter the address of the  video file whose sub you want to download
def ask(parent=None,message='',default_value =''):
	dlg = wx.TextEntryDialog(parent,message,caption='SubX',defaultValue=default_value)
	dlg.ShowModal()
	result = dlg.GetValue()
	dlg.Destroy()
	return result

app = wx.App()
app.MainLoop()

#Message Box to encounter the errors
def showmsg(get_msg,get_title):
	app = wx.App(redirect=False)
	#msg = get_msg
	#title = get_title
	d = PBI.PyBusyInfo(get_msg,title=get_title)
	time.sleep(3)
	d= None
	#d.showmsg()
	return d

if __name__ =='__main__':
	x = ask(message='Enter Tv Series Or Movie name :')
	print x
