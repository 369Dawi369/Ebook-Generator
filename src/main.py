from src.chatgpt import ChatGPT4
from refactorizer import Refactorer
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def main():
	"""Setup"""
	chat = ChatGPT4()

	# Generate outline with parameters in English
	outline_answer = chat.generate_json_from_arguments("Crocheting patterns", page_target=50)
	Refactorer.dump_to_new_json(outline_answer)

	#TODO figure out how use reportlab and the best way to generate the book


if __name__ == '__main__':
	main()
