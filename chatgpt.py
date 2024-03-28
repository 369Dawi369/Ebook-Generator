import openai
import json
import sys



class ChatGPT4:
	def __init__(self):
		self.key = None
		with open("keys.json", 'r') as f:
			data: dict = json.load(f)
			for item in data:
				if item == "OPENAI_API_KEY":
					self.key = data["OPENAI_API_KEY"]
		if not self.key:
			print("No OpenAI API key found!")
			sys.exit(1)


