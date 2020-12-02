import json
import os.path

class SaveGame():
    LOCATION = './data/saved-games/'
    FILENAME = 'game-data.json'
    FULL_PATH = LOCATION + FILENAME

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

    def delete_save_data(self):
        """Removes the save data but preserves our settings"""
        with open(SaveGame.FULL_PATH) as saved_game:
            game_data = json.load(saved_game)

        settings = game_data['settings']
        game_data.clear()
        game_data['settings'] = settings

        with open(SaveGame.FULL_PATH, 'w') as saved_game:
            saved_game.write(json.dumps(game_data))

    def toggle_music_option(self):
        with open(SaveGame.FULL_PATH) as saved_game:
            game_data = json.load(saved_game)

        settings = game_data['settings']
        settings['music'] = not settings['music']

        with open(SaveGame.FULL_PATH, 'w') as saved_game:
            saved_game.write(json.dumps(game_data))

