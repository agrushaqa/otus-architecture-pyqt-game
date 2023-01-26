from features.steps.src.commands.abs_interface.command import Command
from features.steps.src.commands.command_interface.movable import Movable


class MoveCommand(Command):
    def __init__(self, m: Movable):
        self.m = m

    def execute(self):
        self.m.set_position(self.m.add(self.m.get_position(),
                                       self.m.get_velocity()))
