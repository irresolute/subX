import hashlib
import os
import dialog
import requests

# To make hash of the intended video file 
def get_hash(name):
	readsize = 1024*64
	with open(name,'rb') as f:
		size = os.path.getsize(name)
		data = f.read(readsize)
		f.seek(-readsize,os.SEEK_END)
		data += f.read(readsize)
	return hashlib.md5(data).hexdigest()



#use of subDB api
def api(file_add):
	file_hash = hashlib.md5()
	file_hash = get_hash(file_add)
	user_agent = {'User-agent':'SubDB/1.0 (subX/0.1; http://github.com/irresolute/subX)'}
	param  ={'action':'download','hash':file_hash,'language':'en'}
	try:
		r = requests.get("http://api.thesubdb.com/",headers=user_agent,params=param)
	except:
		pass
	if(r.status_code !=200):	
		dialog.showmsg('Subtitle not found check connectivity and try again','subX')

	fName, fExt = os.path.splitext(file_add)
	fName = fName+ '.srt'
	with open(fName,'wb') as f:
    	 f.write(r.text.encode('ascii','ignore'))
file_add = dialog.ask(message='Enter address')
api(file_add)
