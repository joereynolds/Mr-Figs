"""
TODO
Would be nice to load the entire config at once rather
than each time per method
"""
import json
import os.path

class UserData():
    LOCATION = os.path.join('data', 'saved-games' + os.sep)
    FILENAME = 'game-data.json'
    FULL_PATH = LOCATION + FILENAME

    def has_completed_level(self, level: str) -> bool:
        path = UserData.LOCATION + UserData.FILENAME

        with open(path) as saved_game:
            game_data = json.load(saved_game)

        if level in game_data:
            return game_data[level]['completed_level']

        return False

    def get_last_played_level(self) -> str:
        """
        Saves the name of the level we last played so that
        when we head to the level select, we're positioned over it
        """
        path = UserData.LOCATION + UserData.FILENAME

        with open(path) as saved_game:
            game_data = json.load(saved_game)

        try:
            return game_data['last_played_level']
        except KeyError:
            return None

    def register_last_played_level(self, level: str):
        """
        Saves the name of the level we last played so that
        when we head to the level select, we're positioned over it
        """
        path = UserData.LOCATION + UserData.FILENAME

        with open(path) as saved_game:
            game_data = json.load(saved_game)

        game_data['last_played_level'] = level

        with open(path, 'w') as saved_game:
            saved_game.write(json.dumps(game_data))


    def save(self, completed_level: str, turns_taken: int, collected_tape=None):
        """Saves our game"""
        path = UserData.LOCATION + UserData.FILENAME

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
        with open( UserData.FULL_PATH) as saved_game:
            game_data = json.load(saved_game)

        settings = game_data['settings']
        game_data.clear()
        game_data['settings'] = settings

        with open( UserData.FULL_PATH, 'w') as saved_game:
            saved_game.write(json.dumps(game_data))

    def toggle_music_option(self):
        with open( UserData.FULL_PATH) as saved_game:
            game_data = json.load(saved_game)

        settings = game_data['settings']
        settings['music'] = not settings['music']

        with open( UserData.FULL_PATH, 'w') as saved_game:
            saved_game.write(json.dumps(game_data))

    def has_video_for_level(self, level: str):
        with open( UserData.FULL_PATH) as saved_game:
            game_data = json.load(saved_game)

        if level in game_data:
            if 'collected_tape' in game_data[level] and game_data[level]['collected_tape'] == True:
                return True
