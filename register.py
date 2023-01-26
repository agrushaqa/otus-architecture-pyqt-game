from features.environment import mock_add
from features.steps.src.commands.move import MoveCommand
from features.steps.src.commands.rotate import ChangeVelocityCommand
from features.steps.src.commands.start_working_thread import \
    StartBlockedWorkingThread


class RegisterOperations:
    def __init__(self):
        self.current_operation_id = 0
        self.current_object_id = 0
        self.current_game_id = 0

    def register(self, ioc, scope, obj):
        scope.current(ioc)
        ioc.resolve(key="IoC.register",
                    registered_name="Commands.Move",
                    called_method=MoveCommand
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Commands.ChangeVelocity",
                    called_method=ChangeVelocityCommand
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Movable.get_position",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Movable.get_velocity",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Movable.set_velocity",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Movable.set_position",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Rotable.get_direction",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Rotable.set_direction",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Rotable.get_directions_number",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Rotable.set_directions_number",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Rotable.get_angular_velocity",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Rotable.set_angular_velocity",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="OperationId.set_id",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Operation.get_id",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="OperationId.set_entity",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Operation.get_entity",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="OperationId.set_name",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Operation.get_name",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Operation.set_entity",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Operation.get_entity",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.set_id",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.get_id",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.set_entity",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.get_entity",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.set_name",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.get_name",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.set_list_operations",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Object.get_list_operations",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Game.set_id",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Game.get_id",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Game.get_list_objects",
                    called_method=obj.get_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Game.set_list_objects",
                    called_method=obj.set_property
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="Movable.add",
                    called_method=mock_add
                    ).execute()

        ioc.resolve(key="IoC.register",
                    registered_name="StartBlockedThreadCommand",
                    called_method=StartBlockedWorkingThread).execute()

    def add_operation(self, ioc, game_id, object_id, operation):
        self.current_operation_id += 1
        self._add_operation_to_object(ioc, game_id, object_id)

        ioc.resolve("Operation.set_entity",
                    f"{game_id}.{object_id}.{self.current_operation_id}"
                    ".operation_id",
                    operation
                    ).execute()
        return self.current_operation_id

    def _add_operation_to_object(self, ioc, game_id, object_id):
        object_list_operations: list = ioc.resolve(
            "Object.get_list_operations",
            f"{game_id}.{object_id}_list_operations").execute()
        if object_list_operations is None:
            object_list_operations = [self.current_operation_id]
        else:
            object_list_operations.append(self.current_operation_id)
        ioc.resolve(
            "Object.set_list_operations",
            f"{game_id}.{object_id}_list_operations",
            object_list_operations).execute()

    def get_operation_name(self, ioc, game_id, object_id, operation_id):
        return ioc.resolve("Operation.get_name",
                           f"{game_id}.{object_id}.{operation_id}"
                           ".operation_id").execute()

    def add_object(self, ioc, game_id, object_name, object):
        self.current_object_id += 1
        self._add_object_to_game(ioc, game_id)
        ioc.resolve("Object.set_entity",
                    f"{game_id}.{self.current_object_id}"
                    ".object_id",
                    object
                    ).execute()
        ioc.resolve("Object.set_name",
                    f"{game_id}.{self.current_object_id}"
                    ".object_id",
                    object_name
                    ).execute()
        return self.current_object_id

    def _add_object_to_game(self, ioc, game_id):
        game_list_objects: list = ioc.resolve(
            "Game.get_list_objects",
            f"{game_id}._list_objects").execute()
        if game_list_objects is None:
            game_list_objects = [self.current_operation_id]
        else:
            game_list_objects.append(self.current_operation_id)
        ioc.resolve(
            "Game.set_list_objects",
            f"{game_id}._list_objects",
            game_list_objects).execute()

    def get_Last_object_id(self):
        return self.current_object_id

    def get_Last_operation_id(self):
        return self.current_operation_id
