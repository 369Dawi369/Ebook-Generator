import json
import sys
import os
import ast
from openai import OpenAI


class ChatGPT4:
	def __init__(self):
		with open("jsons/keys.json", 'r') as f:
			data: dict = json.load(f)
			for item in data:
				if item == "OPENAI_API_KEY":
					os.environ['OPENAI_API_KEY'] = data["OPENAI_API_KEY"]
				else:
					print("No OpenAI API key found!")
					sys.exit(1)

		self.client = OpenAI()
		self.base_3_5_model = "gpt-3.5-turbo-0125"
		self.instruction_target_audience = "middle aged czech women living in the czech republic"
		self.pages_target = 250

	def generate_json_from_arguments(self, topic: str, temperature: float = 0.7) -> dict:
		with open("jsons/example.json", 'r') as f:
			book_data = json.load(f)

		prompt = f"""
You one task is to generate a captivating book outline in english in the form of a json file in the exact format as 
this {book_data}. You will write it on the topic of '{topic}' and it will be specifically targeted
towards {self.instruction_target_audience}. You should aim to keep it around {self.pages_target} pages.
"""

		response = self.client.chat.completions.create(
			model=self.base_3_5_model,
			response_format={"type": "json_object"},
			temperature=temperature,
			messages=[
				{"role": "system", "content": "You are a straightforward assistant designed to output JSON."},
				{"role": "user", "content": prompt}
			]
		)

		str_back: str = response.choices[0].message.content
		dict_obj: dict = ast.literal_eval(str_back)
		return dict_obj
