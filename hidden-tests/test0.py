test = {
	"name": "test0",
	"points": 1,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> def errorr():
					...	 try:
					...		 Fortune=Student(2.0,12.4,3.0)
					...	 except AssertionError:
					...		 return True
					...	 except:
					...		 return False
					...	 return False
					>>> errorr()
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