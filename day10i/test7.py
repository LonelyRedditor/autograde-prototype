test = {
	"name": "test7",
	"points": 2,
	"hidden": True,
	"suites": [
		{
			"cases": [
				{
					"code": r"""
					>>> "Student" in dir() and "average" in dir()
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> def errorr():
					...	 try:
					...		 Fortune=Student(23,4.50,6.70)
					...		 Joba=Student(21,45.67,3.40)
					...		 average([Joba,Fortune,'3'])
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