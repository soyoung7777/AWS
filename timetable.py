import urllib.request
import urllib.parse
import json

def main():

	odAPI = "https://api.odsay.com/v1/api/"	

	start = "서울고속"
	encS = urllib.parse.quote_plus(start)
	end = "부산서부"
	encE = urllib.parse.quote_plus(end)

	my = "n+1iCTjka3qgrhco9Xl3e05Depf0hpct6SJUYUEH38E"
	encMy = urllib.parse.quote_plus(my)

	odSUrl = odAPI+"expressBusTerminals?&terminalName="+encS+"&apiKey="+encMy
	odEUrl = odAPI+"expressBusTerminals?&terminalName="+encE+"&apiKey="+encMy

	s_request = urllib.request.Request(odSUrl)
	s_response = urllib.request.urlopen(s_request)
	json_rt_s = s_response.read().decode('utf-8')
	data_s = json.loads(json_rt_s)
	sID = str(data_s['result'][0]['stationID'])
	
	e_request = urllib.request.Request(odEUrl)
	e_response = urllib.request.urlopen(e_request)
	json_rt_e = e_response.read().decode('utf-8')
	data_e = json.loads(json_rt_e)
	eID = str(data_e['result'][0]['stationID'])

	

	tUrl = odAPI+"expressServiceTime?&startStationID="+sID+"&endStationID="+eID+"&apiKey="+encMy
	
	request = urllib.request.Request(tUrl)
	response = urllib.request.urlopen(request)
	json_rt = response.read().decode('utf-8')
	data = json.loads(json_rt)
	
	schedule = data['result']['station'][0]['schedule']

	print(schedule)

if __name__ == '__main__':
	main()
