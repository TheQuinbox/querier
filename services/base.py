from abc import ABC, abstractmethod

class BaseService(ABC):
	name = "Service"
	
	@staticmethod
	@abstractmethod
	def get_results(text):
		pass
