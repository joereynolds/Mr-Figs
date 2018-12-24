import json
import os.path

class SaveGame(object):

    LOCATION = '../data/saved-games/'
    FILENAME = 'mr-figs.json'

    def create(path):
        """Creates an empty save file"""
        if os.path.exists(path):
            return
        open(path, 'w')

    def save():
        """Saves the game"""
        pass


