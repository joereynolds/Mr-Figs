import json
import os.path

class SaveGame():
    LOCATION = './data/saved-games/'
    FILENAME = 'mr-figs.json'

    def save(self, completed_level: str):
        """Saves our game"""
        path = SaveGame.LOCATION + SaveGame.FILENAME

        with open(path) as saved_game:
            game_data = json.load(saved_game)

        if completed_level not in game_data['completed_levels']:
            game_data['completed_levels'].append(completed_level)

        with open(path, 'w') as saved_game:
            saved_game.write(json.dumps(game_data))

