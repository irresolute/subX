'''To get the first 64 bit and last 64 bit of the video file and hash it  '''
import hashlib
import os
import dialog
import requests

def get_hash(name):
	readsize = 1024*64
	with open(name,'rb') as f:
		size = os.path.getsize(name)
		data = f.read(readsize)
		f.seek(-readsize,os.SEEK_END)
		data += f.read(readsize)
	return hashlib.md5(data).hexdigest()


#actions pert	aining to the subDB api

def api(file_add):
	#file_hash = get_hash(file_name)
	file_hash = hashlib.md5()
	file_hash = get_hash(file_add)
	print file_hash	

	User_Agent = {'user-agent':'SubDB/1.0 (subX/0.1; http://github.com/irresolute/subX)'}
	urlparams  ={'actions':'download','hash':file_hash,'language':'en'}
	#making the download request from the subDB
	
	r = requests.get('http://api.thesubdb.com/',headers=User_Agent,params=urlparams)
	print r.encoding
	
	print r.encoding
	print r.status_code
	print r.content
	print r.text.encode('ascii','ignore')
	fName, fExt = os.path.splitext(file_add)
	fName = fName + '.srt'
	with open(fName,'wb') as f:
    	 f.write(r.text.encode('ascii','ignore'))
    #print r.status_code
    #open(fName,'r')

file_add = dialog.ask(message='Enter address')
api(file_add)
