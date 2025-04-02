from unidecode import unidecode
import re


def normalize_title(title):

    title = unidecode(title)
    title = title.lower()
    title = title.replace(" ", "-")
    title = re.sub(r'[^a-zA-Z0-9-]', '', title)

    return title


def normalize_word(word):

    word = word.lower()
    word = re.sub(r'[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ]', '', word)

    return word


def normalize_text(text):

    text = text.lower()
    text = re.sub(r'[^a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ ]', '', text)

    return text
