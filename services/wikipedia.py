from .base import BaseService
import wikipedia
from wikipedia.exceptions import DisambiguationError

class WikipediaService(BaseService):
	name = "Wikipedia Search"
	
	def get_results(text):
		try:
			suggested = wikipedia.suggest(text)
			page = None
			if suggested is not None:
				page = wikipedia.page(suggested)
			if page is not None:
				return f"{page.title}:\n{page.summary.strip()}\n"
			else:
				return "Too many results. Possible queries include:\n" + "\n".join(wikipedia.search(text)) + "\n"
		except DisambiguationError as e:
			return "\n".join(e.options)
