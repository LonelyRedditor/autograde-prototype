test = {
	"name": "test3",
	"points": 1,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> 'stof' in dir() and 'stoi' in dir() and 'itos' in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> def error(i):
					...	 try:
					...		 itos(i)
					...	 except:
					...		 return True
					...	 return False
					>>> error('12345')
					True
					""",
					"hidden": False,
					"locked": False,
				}, 
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}
	]
}