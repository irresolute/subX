import requests
def download_sub(file_hash):
	file_hash = get_hash()
	params = {action:"download",hash:file_hash,language=en}
	try:
		r = requests.get("http://sandbox.thsubdb.com/",params)
	except 404:
		print 
