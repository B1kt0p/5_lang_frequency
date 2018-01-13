import argparse
import re
import collections


def get_argv():
    parser = argparse.ArgumentParser(
        description="Частотный анализ слов в тексте"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Путь до текстового файла"
    )
    return parser.parse_args().file


def load_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except (FileNotFoundError, UnicodeDecodeError):
        return None


def get_most_frequent_words(text):
    text = text.lower()
    compile_re = re.compile(r"\W+", re.UNICODE)
    word_list = re.split(compile_re, text)
    # Если будут не алфовитно-цифровой символ в начале текста или в конце,
    # то первый и последний элемент списка будет ""
    if word_list[0] == "":
        word_list.pop(0)
    if word_list[-1] == "":
        word_list.pop()
    number_most_frequent_words = 10
    most_frequent_words = collections.Counter(word_list).most_common(number_most_frequent_words)
    return most_frequent_words


if __name__ == '__main__':
    file_path = get_argv()
    text = load_data(file_path)
    if text:
        most_frequent_words = get_most_frequent_words(text)
        for most_frequent_word in most_frequent_words:
            print("'{0}' упоменается {1} раз".format(
                most_frequent_word[0], most_frequent_word[1]
            ))
    else:
        print("Путь до файла введен не верно!")
