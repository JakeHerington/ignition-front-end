def doGet(request, session):

	import system
	
	result = system.dataset.toPyDataSet(system.db.runNamedQuery("TodayOutput", {})) 
	res = system.util.jsonEncode(result)
	
	request["servletResponse"].addHeader("Access-Control-Allow-Origin", "http://localhost:3000")
	
	return {'json': res}