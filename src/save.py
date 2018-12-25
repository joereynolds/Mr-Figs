import json
import os.path

class SaveGame(object):

    LOCATION = '../data/saved-games/'
    FILENAME = 'mr-figs.json'

    def create(path: str):
        """Creates an empty save file"""
        if os.path.exists(path):
            return
        save = open(path, 'w')

        initial_save = {
            'completed_levels': ['level-0']
        }
        save.write(json.dumps(initial_save))

    def save():
        """Saves the game"""
        pass


