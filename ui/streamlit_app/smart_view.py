from core.config.gpt import GPTConfig
from core.utils.common_utils import load_json_file

config = GPTConfig.from_dict(load_json_file("config/gpt.json"))

