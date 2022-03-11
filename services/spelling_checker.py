from .base import BaseService
from spellchecker import SpellChecker

class SpellingCheckerService(BaseService):
	name = "Spelling Checker"
	
	def get_results(text):
		spell = SpellChecker()
		misspelled = spell.unknown(text.split(" "))
		ret = ""
		for word in misspelled:
			ret += word + ":\n"
			for suggestion in spell.candidates(word):
				ret += suggestion + "\n"
			ret += "\n"
		return ret
