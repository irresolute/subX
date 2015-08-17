import wx

def ask(parent=None,message='',default_value =''):
	dlg = wx.TextEntryDialog(parent,message,caption='SubX',defaultValue=default_value)
	dlg.ShowModal()
	result = dlg.GetValue()
	dlg.Destroy()
	return result

app = wx.App()
app.MainLoop()

if __name__ =='__main__':
	x = ask(message='Enter Tv Series Or Movie name :')
	print x
