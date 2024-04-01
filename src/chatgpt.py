import json
import sys
import os
import ast
from openai import OpenAI


class ChatGPT4:
	def __init__(self):
		with open("../jsons/keys.json", 'r') as f:
			data: dict = json.load(f)
			for item in data:
				if item == "OPENAI_API_KEY":
					os.environ['OPENAI_API_KEY'] = data["OPENAI_API_KEY"]
				else:
					print("No OpenAI API key found!")
					sys.exit(1)

		self.client = OpenAI()
		self.base_3_5_model = "gpt-3.5-turbo-0125"
		self.target_audience = "middle aged czech women living in the czech republic"
		self.language = "English"

	def generate_json_from_arguments(self, topic: str, page_target: int = 250, temperature: float = 0.7) -> dict:
		with open("../jsons/example_outline.json", 'r') as f:
			book_data = json.load(f)

		prompt = f"""
You one task is to generate a captivating ebook outline in english in the form of a json file in the exact format as 
this {book_data}. You will decide the number of chapters and pages per chapter. You will write it on the topic of 
'{topic}' and it will be specifically targeted towards {self.target_audience}. You should aim to keep
it around {page_target} pages.
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

	def generate_chapters(self) -> dict:
		collective_chapters = {}
		with open("../jsons/temp_outline.json", 'r') as f:
			outline = json.load(f)
			for chapter in outline["chapters"]:
				collective_chapters[str(chapter["chapterNumber"]) + " " + chapter["title"]] = self.generate_chapter(chapter)
		return collective_chapters

	def generate_chapter(self, chapter, temperature: float = 0.7) -> dict:
		chapter_dict = {}
		with open("../jsons/temp_outline.json", 'r') as f:
			outline = json.load(f)

		for subsection in chapter["subsections"]:
			prompt = f"""
You are a part of the effort to write this book. The outline of the book looks like this {outline}.
You only job is to take into account the rest of the outline, and only focus on your subsection named 
{subsection["title"]}. It should be {subsection["pages"]} long and be funny, entertaining, and captivating. 
			"""

			response = self.client.chat.completions.create(
				model=self.base_3_5_model,
				temperature=temperature,
				messages=[
					{"role": "system", "content": "You are a lovable writer that aims to write great and helpful"
					                              " content"},
					{"role": "user", "content": prompt}
				]
			)
			str_back: str = response.choices[0].message.content
			chapter_dict[subsection["title"]] = str_back
		return chapter_dict


	def generate_into(self, temperature: float = 0.7) -> str:
		#Too short
		with open('../jsons/temp_outline.json', 'r') as f:
			data = json.load(f)

		prompt = f"""
You are given the outline of a book: {data}. Your task is to write an imaginative, captivating, and funny medium length
into for the ebook that should be decently long. The target audience for this ebook is {self.target_audience} and you 
will do it in the {self.language} language. The into should not include any details about the book and should begin 
with the first sentence of the book. 
		"""

		response = self.client.chat.completions.create(
			model=self.base_3_5_model,
			temperature=temperature,
			messages=[
				{"role": "system", "content": "You are a lovable writer that aims to write great and helpful"
				                              " content"},
				{"role": "user", "content": prompt}
			]
		)

		str_back: str = response.choices[0].message.content
		return str_back

	def generate_conclusion(self, temperature: float = 0.7) -> str:
		# Also too short
		with open('../jsons/temp_outline.json', 'r') as f:
			data = json.load(f)

		prompt = f"""
You are given the outline of a book: {data}. Your task is to write an imaginative, captivating, and funny medium length
conclusion for the ebook that should be decently long. The target audience for this ebook is {self.target_audience} and you 
will do it in the {self.language} language. The into should not include any details about the book and should begin 
with the first sentence of the conclusion. 
		"""

		response = self.client.chat.completions.create(
			model=self.base_3_5_model,
			temperature=temperature,
			messages=[
				{"role": "system", "content": "You are a lovable writer that aims to write great and helpful"
				                              " content"},
				{"role": "user", "content": prompt}
			]
		)

		str_back: str = response.choices[0].message.content
		return str_back

	@staticmethod
	def change_details():
		with open('../jsons/temp_outline.json', 'r') as f:
			data = json.load(f)

		data["author"] = "David W Erwin"
		data["publicationYear"] = 2024

		with open('../jsons/temp_outline.json', 'w') as f:
			json.dump(data, f, indent=4)
