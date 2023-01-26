from features.steps.src.commands.ubject2d import UObject2D

# import json
# import register
# from features.steps.src.commands.start_working_thread import ThreadConfig


class Game:
    def __init__(self, obj: UObject2D):
        self.game_list = []
        self.last_game_id = 0
        self.obj = obj

    def new_game(self, name):
        self.last_game_id += 1
        self.game_list.append(self.last_game_id)
        self.obj.set_property("Game.last_game_id", self.last_game_id)
        self.obj.set_property("Game.list_game_ids", self.game_list)
        self.obj.set_property(f"Game.name.{self.last_game_id}", name)
        self.obj.set_property(f"Game.id.{name}", self.last_game_id)
        self.obj.set_property(f"{self.last_game_id}._list_objects", [])
        return self.last_game_id
