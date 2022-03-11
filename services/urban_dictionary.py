from .base import BaseService
import requests

class UrbanDictionaryService(BaseService):
	name = "Urban Dictionary Search"
	
	def get_results(text):
		r = requests.get("http://api.urbandictionary.com/v0/define", params={"term": text})
		try:
			json = r.json()
		except ValueError as e:
			raise ValueError(f"Error parsing json response. {e}")
		try:
			ret = ""
			for entry in json["list"]:
				ret += f"{entry['word']}:\n{entry['definition']}\nExample: {entry['example']}\n\n"
		except KeyError as e:
			raise KeyError(f"Error parsing result: {e}")
		return ret
