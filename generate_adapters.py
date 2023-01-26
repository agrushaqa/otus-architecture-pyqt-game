import os

from features.steps.src.adapter.adapter import GeneratorAdapter
from features.steps.src.commands.command_interface.movable import Movable
from features.steps.src.commands.command_interface.rotable import Rotable

# можно генерировать на основе inspect и importlib.util
# но я подумал, что лучше список команд явно передавать


def generate_adapters(target_path, list_classes):
    for i_clazz in list_classes:
        generator = GeneratorAdapter()
        generator.set_target_dir(target_path)
        generator.set_filename(
            f"autogen_adapter_{i_clazz.__module__.split('.')[-1]}.py")
        generator.set_clazz(i_clazz)
        generator.execute()


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    target_path = os.path.join(
        current_dir,
        "features",
        "steps",
        "src",
        "commands",
        "generated_adapters"
    )
    generate_adapters(target_path, [Movable, Rotable])
