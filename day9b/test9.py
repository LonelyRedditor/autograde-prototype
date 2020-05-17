test = {
	"name": "test9",
	"points": 2,
	"hidden": True,
	"suites": [ 
		{
			"cases": [ 
				{
                    "code": r"""
                    >>> "fibSum" in dir()
                    True
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> import time	
                    >>> evenFibs = lambda n: (((5 * n**2+4)**0.5)%1==0 or ((5 * n**2-4)**0.5)%1==0)
                    >>> def fibSumm(n):
                    ...     return sum(list(filter(evenFibs, range(2,n+1, 2))))
                    >>> alpha = time.time()
                    >>> y = fibSumm(1_000_000)
                    >>> omega = time.time()
                    >>> bound=round(omega-alpha,4)+0.0032
                    >>> start = time.time()
                    >>> x = fibSumm(1_000_000)
                    >>> end = time.time()
                    >>> diff= end-start
                    >>> diff < bound
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