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
    return parser.parse_args()


def load_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except (FileNotFoundError, UnicodeDecodeError):
        return None


def get_most_frequent_words(text):
    text = text.lower()
    word_list = re.findall(r"\w+", text)
    number_most_frequent_words = 10
    frequent_words = collections.Counter(word_list)
    most_frequent_words = frequent_words.most_common(
        number_most_frequent_words
    )
    return most_frequent_words


if __name__ == "__main__":
    file_path = get_argv().file
    text = load_data(file_path)
    if text:
        most_frequent_words = get_most_frequent_words(text)
        print("10 самых популярных слов в тексте:")
        for word, count in most_frequent_words:
            print("'{}' - {} слов".format(word, count))
    else:
        print("Путь до файла введен не верно!")
