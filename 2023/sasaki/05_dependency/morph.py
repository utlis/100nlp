from typing import TypedDict


class MorphInitArgs(TypedDict):
    base: str
    surface: str
    pos: str
    pos1: str


class Morph(object):
    def __init__(self, init_args: MorphInitArgs) -> None:
        self.surface = init_args['surface']
        self.base = init_args['base']
        self.pos = init_args['pos']
        self.pos1 = init_args['pos1']

    def to_str(self) -> str:
        return f"{self.surface},{self.base},{self.pos},{self.pos1}"
