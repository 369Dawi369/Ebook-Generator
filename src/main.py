from src.chatgpt import ChatGPT4
from refactorizer import Refactorer




def main():
	"""Setup"""
	chat = ChatGPT4()
	chat.language = "English"

	# Generate outline with parameters in English
	outline_answer = chat.generate_json_from_arguments("How to have lovely grandchildren", page_target=50)
	Refactorer.dump_to_temp_json(outline_answer)

	#TODO generate the actual content
	chat.change_details()
	book = {"chapters": chat.generate_chapters(), "intro": chat.generate_into(),
	        "conclusion": chat.generate_conclusion()}
	Refactorer.dump_book(book)

	#TODO figure out how use reportlab and the best way to generate the book




if __name__ == '__main__':
	main()
