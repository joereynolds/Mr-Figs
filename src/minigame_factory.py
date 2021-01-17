from src.minigames.hunt.game import Hunt
from src.minigames.lines.game import Lines

class MinigameFactory():

    def build(self, minigame: str, previous_scene):
        minigames = {
            'hunt': Hunt,
            'lines': Lines,
        }

        return minigames[minigame](previous_scene)

