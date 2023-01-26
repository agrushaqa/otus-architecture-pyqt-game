from features.steps.src.commands.abs_interface.uobject import UObject


class UObject2D(UObject):
    def __init__(self):
        self.obj = {}

    def get_property(self, key: str):
        try:
            return self.obj[key]
        except Exception:
            return None

    def set_property(self, key: str, new_value):
        self.obj[key] = new_value

    def list_keys(self):
        return self.obj.keys()
