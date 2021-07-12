def doGet(request, session):

	import system
	
	res = {
		"value": system.tag.read("[default]_Weather_Sensor_/Plant1/HmiyD2TTLFNqkNe/AMBIENT_TEMPERATURE").value
		}
	
	request["servletResponse"].addHeader("Access-Control-Allow-Origin", "http://localhost:3000")
	
	return {'json': res}