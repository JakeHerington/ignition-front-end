def doGet(request, session):

	import system
	
	SOURCE_KEY = request["params"]["srckey"]
	tags = ["AC_POWER", "AMPERAGE", "DAILY_YIELD", "DATE_TIME", "DC_POWER", "POWER_FACTOR", "REACTIVE_POWER", "POWER_FACTOR", "VOLTAGE"]
	tagPath = "[default]_Solar Plant with Time_/Plant1/" + SOURCE_KEY + "/"
	res = []
	
	for tag in tags:
		entry = {
			"id": len(res),
			"tagName": tag,
			"tagValue": system.tag.read(tagPath + tag).value
			}
		res.append(entry)
	
	request["servletResponse"].addHeader("Access-Control-Allow-Origin", "http://localhost:3000")
	
	return {'json': res}