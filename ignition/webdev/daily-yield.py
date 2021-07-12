def doGet(request, session):

	import system
	
	tagPaths = system.tag.browseTags(parentPath="[default]_Solar Plant with Time_/Plant1/")
	res = []
	
	for tagPath in tagPaths:
		value = system.tag.read(str(tagPath.fullPath) + "/DAILY_YIELD").value
		res.append(value)
	
	request["servletResponse"].addHeader("Access-Control-Allow-Origin", "http://localhost:3000")
	
	return {'json': res}