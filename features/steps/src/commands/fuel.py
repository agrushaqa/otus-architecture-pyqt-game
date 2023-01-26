from features.steps.src.commands.abs_interface.command import (
    Command, CommandException)
from features.steps.src.commands.composite_command import CompositeCommand
from features.steps.src.commands.move import Movable, MoveCommand


class Fuel:
    def __init__(self):
        self.value = 0
        self.consumption = 0

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def get_consumption(self):
        return self.consumption

    def set_consumption(self, value):
        self.consumption = value


class CheckFuelCommand(Command):
    def __init__(self, value: Fuel, min_value=0):
        self.value = value
        self.min_value = min_value

    def execute(self) -> None:
        checked_fuel = self.value.get()
        if checked_fuel < self.min_value:
            raise CommandException


class BurnFuelCommand(Command):
    def __init__(self, value: Fuel):
        self.value = value

    def execute(self) -> None:
        old_value = self.value.get()
        self.value.set(old_value - self.value.get_consumption())


class FuelMovement(Command):
    def __init__(self, m: Movable, fuel: Fuel):
        self.fuel = fuel
        self.command_list = CompositeCommand(
            [CheckFuelCommand(self.fuel, self.fuel.get_consumption()),
             MoveCommand(m),
             BurnFuelCommand(self.fuel)])

    def execute(self) -> None:
        self.command_list.execute()
