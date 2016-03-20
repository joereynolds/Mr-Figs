import game
import environment

if __name__ == '__main__':
    game = game.Game(60)
    game.run(environment.level_obj_list[0])

