# querier

Query information quickly and easily.

## Adding a service.

Adding services was made simple with the power of Python!

A sample service is below:

```python
from .base import BaseService

class MyService(BaseService):
	name = "Display name in the list"
	
	def get_results(text):
		# Get information from your service, and return it as an str.
```

Once your service is constructed, import it services/__init__.py, and add the class name to supported_services. No need to instantiate it though (the classes and their methods are static).

**Note**: Wherever you put your service in supported_services is where it will appear in the list in the GUI. Keep this in mind!
