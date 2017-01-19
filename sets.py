COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(inset):
	listo=[]
	for key, value in COURSES.items():
		if not value.isdisjoint(inset):
			listo.append(key)
	return listo
	
def covers_all(inset):
	listo=[]
	for key, value in COURSES.items():
		if inset.issubset(value):
			listo.append(key)
	return listo


