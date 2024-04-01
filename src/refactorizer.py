import json


class Refactorer:
	@staticmethod
	def dump_to_temp_json(completion: dict):
		with open("../jsons/temp_outline.json", 'w') as f:
			json.dump(completion, f, indent=4)

	@staticmethod
	def clean_up_temp_json():
		with open("../jsons/temp_outline.json", 'w') as f:
			f.write('')

	@staticmethod
	def dump_book(completion):
		with open("../jsons/temp_book.json", 'w') as f:
			json.dump(completion, f, indent=4)