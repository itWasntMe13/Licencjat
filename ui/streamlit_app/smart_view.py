from core.config.gpt import GPTConfig
from core.utils.common_utils import load_json_file
import streamlit as st


config = GPTConfig.from_dict(load_json_file("config/gpt.json"))

def show():
