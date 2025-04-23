import streamlit as st
import sys
import os
from pathlib import Path

from core.services.gpt.gpt_config_service import GptConfigService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from core.config import BOOKS_DIR
from core.utils.common_utils import load_json_file
from core.models.books.book import Book
from core.config.gpt import GptConfig
from core.services.books.book_index_service import BookIndexService
from core.services.books.book_detail_service import BookDetailService
from core.services.books.book_service import BookService
from core.utils.gpt_utils import count_tokens


def show():
    st.title("Smart View")
    st.write("W budowie...")