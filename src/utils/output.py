import json 
from functools import wraps

def beautify_json(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		result = func(*args, **kwargs)
		str = json.dumps(result, indent=4, sort_keys=True)
		print(f"Here's the output for {func.__name__}, {str}")
		return result 
	return wrapper
