# Autograde-prototype (v0.9)

This is an API created for handling the grading of python submissions in ECX's 30DaysOfCode Challenge.

## Usage

1. Clone the repo and put your test cases in the Hidden-Beginner or hidden-tests folder

* A test file with name q1.py and score 8 should contain this:
```
test = {
	"name": "q1",
	"points": 8,
	"hidden": False,
	"suites": [ 
		{
			"cases": [ 
				{
					"code": r"""
					>>> main(8, 12) == 4
					True
					""",
					"hidden": False,
					"locked": False,
				} 
			],
			"scored": False,
			"setup": "",
			"teardown": "",
			"type": "doctest"
		}
	]
}
```
What basically happens is that each of the code block is tested against the user submission and scored if it matches the output.
N.B: multiple code blocks are possible and can be used in cases where its all or nothing. They should look like this:
```
...
	...
		"cases": [ 
				{
					"code": r"""
					>>> main(8, 12) == 4
					True
					""",
					"hidden": False,
					"locked": False,
				},
				{
					"code": r"""
					>>> main(6, 12) == 6
					True
					""",
					"hidden": False,
					"locked": False,
				} 
			],
	...
...
```


2. File to be graded and user's namee server is sent in a form through a POST request to th and the grade is sent back as response ========> This can be integrated with AJAX PHP on each user dashboard, granting access to instanteneous grading.


## Constraints
 * All users must submit with the exact same function name as the test file in order to avoid problems
 * Go Crazy and break it, It helps us see the weak points in the application. 


suggestions are welcome and should be directed to [Geektutor](mailto:sodiq.akinjobi@gmail.com)
