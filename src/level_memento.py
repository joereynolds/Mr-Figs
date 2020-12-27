class LevelMemento:
    def __init__(self, state):
        self.state = state

    def restore(self):
        return self.state
