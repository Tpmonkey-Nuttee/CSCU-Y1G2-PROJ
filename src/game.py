# from db import db # Not used, yet
from classes.player import Player


class Game:
    def __init__(self, username: str) -> None:
        self.username = username.lower()
        self.player = Player(self.username)