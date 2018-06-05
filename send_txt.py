import os.path
import sys
import urllib.request
import json

try:
	import apiai
except ImportError:
	sys.path.append(
		os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
	)
	import apiai

CLIENT_ACCESS_TOKEN = '33615c11c39546908fd8ab5b32dfac16'

def main():
	ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

	request = ai.text_request()

	request.lang = 'de'

	request.session_id = "123"

	txt = "XXX에서 ZZZ까지 경로"
	
	request.query = txt

	response = request.getresponse()
	
	rData = response.read()
	data = rData.decode('utf-8')

	print(data)
	

if __name__ == '__main__':
	main()
