from enum import Enum

class GptModelInfo(Enum):
    GPT_4O_MINI = ( # Najlepszy model do naszych zastosowań. Duży kontekst, niskie koszty,
        "gpt-4o",
        128000,
        0.005,
        0.015
    )
    GPT_3_5_TURBO = (
        "gpt-3.5-turbo", # nazwa modelu
        16384, # maksymalny kontekst
        0.0005,  # input na 1k tokenów w dolcach
        0.0015   # output na 1k tokenów w dolcach
    )
    GPT_4 = (
        "gpt-4",
        8192,
        0.03,
        0.06
    )
    GPT_4_32K = (
        "gpt-4-32k",
        32768,
        0.06,
        0.12
    )
    GPT_4_O = (
        "gpt-4o",
        128000,
        0.005,
        0.015
    )

    def __init__(self, model_name, context_window, input_cost, output_cost):
        self._model_name = model_name
        self._context_window = context_window
        self._input_cost = input_cost
        self._output_cost = output_cost

    @property
    def model_name(self):
        return self._model_name

    @property
    def context_window(self):
        return self._context_window

    @property
    def input_cost(self):
        return self._input_cost

    @property
    def output_cost(self):
        return self._output_cost
