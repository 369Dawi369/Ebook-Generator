import json


class Refactorer:
	@staticmethod
	def dump_to_new_json(completion: dict):
		with open("jsons/temp.json", 'w') as f:
			json.dump(completion, f, indent=4)

	@staticmethod
	def clean_up_temp_json():
		pass
