import json
import os.path

class SaveGame():
    LOCATION = './data/saved-games/'
    FILENAME = 'mr-figs.json'

    def save(self, completed_level: str, turns_taken: int, collected_tape=None):
        """Saves our game"""
        path = SaveGame.LOCATION + SaveGame.FILENAME

        with open(path) as saved_game:
            game_data = json.load(saved_game)

        game_data[completed_level] = {
            'completed_level': True,
            'turns_taken': turns_taken
        }

        if collected_tape is not None:
            game_data[completed_level]['collected_tape'] = collected_tape

        with open(path, 'w') as saved_game:
            saved_game.write(json.dumps(game_data))

