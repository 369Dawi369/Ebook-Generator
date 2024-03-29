from chatgpt import ChatGPT4
from refactorizer import Refactorer


def main():
	chat = ChatGPT4()
	outline_answer = chat.generate_json_from_arguments("How to succeed in life")
	Refactorer.dump_to_new_json(outline_answer)


if __name__ == '__main__':
	main()
