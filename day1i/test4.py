test = {
	"name": "test4",
	"points": 5,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> 'average' in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
					"code": r"""
					>>> a=[36, 71, 95, 68, 49, 37, 53, 11, 40, 32, 68, 84, 50, 62, 63, 25, 56, 44, 26, 64, 57, 35, 60, 54, 55, 81, 44, 24, 36, 96, 64, 88, 21, 55, 31, 33, 100, 73, 76, 42, 69, 17, 84, 49, 42, 8, 5, 13, 49, 26, 13, 6, 55, 2, 19, 87, 46, 29, 25, 54, 58, 85, 68, 21, 22, 23, 26, 54, 90, 15, 10, 72, 68, 99, 68, 3, 85, 95, 63, 90, 41, 3, 31, 24, 1, 38, 1, 1, 51, 69, 37, 49, 6, 36, 1, 71, 40, 20, 71, 78, 37, 67, 85, 6, 15, 77, 8, 4, 94, 80, 26, 100, 11, 46, 72, 89, 59, 64, 58, 7, 96, 91, 100, 37, 79, 7, 82, 1, 4, 78, 75, 91, 93, 40, 40, 29, 75, 76, 44, 100, 62, 62, 26, 82, 84, 95, 2, 1, 44, 15, 18, 41, 7, 69, 28, 37, 86, 40, 95, 86, 60, 27, 15, 79, 29, 19, 37, 77, 4, 29, 95, 78, 59, 15, 38, 81, 15, 2, 46, 14, 40, 96, 81, 44, 21, 57, 61, 5, 83, 13, 82, 90, 87, 7, 41, 72, 28, 9, 77, 32]
					>>> a=list(map(str,a))
					>>> a=' '.join(a)
					>>> round(average(a),2)
					48.55
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
