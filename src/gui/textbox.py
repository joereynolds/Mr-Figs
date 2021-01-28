from typing import List

class Textbox():

    def __init__(self, lines: List[str]):
        self.index = 0
        self.text = lines

    def increment(self):
        self.index += 1

