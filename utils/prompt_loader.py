from pathlib import Path


class PromptLoader:

    @staticmethod
    def load(filename):

        path = Path("prompts") / filename

        with open(path, "r", encoding="utf-8") as file:

            return file.read()