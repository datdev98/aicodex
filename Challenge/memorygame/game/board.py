import random
import requests
import json
from .card import Card
from .player import Player

class Board:
    def __init__(self, size=4):
        self.size = size
        self.cards = []
        self.players = [Player("Player 1"), Player("Player 2")]

    def initialize(self):
        characters = self.fetch_characters()
        selected_chars = random.sample(characters, self.size * self.size // 2)
        self.cards = [Card(char['name'], char['image']) for char in selected_chars * 2]
        random.shuffle(self.cards)

    def fetch_characters(self):
        with open('static/characters.json', 'r', encoding='utf-8') as file:
            characters = json.load(file)
            return [{'name': char['name'], 'image': char['image']} for char in characters]
        return []

    def get_grid(self):
        return [self.cards[i:i + self.size] for i in range(0, len(self.cards), self.size)]
