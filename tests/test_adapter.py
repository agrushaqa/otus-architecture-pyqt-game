import os

from features.steps.src.adapter.adapter import GeneratorAdapter
from features.steps.src.adapter.class_info import ClassInfo
from tests.test_data.imovable import TankOperationsIMovable

#
# class TestAdapter:
#     def test_generate_class_by_interface(self):
#         current_dir = os.path.dirname(os.path.realpath(__file__))
#         target_path = os.path.join(
#             current_dir,
#             "test_data"
#         )
#         generator = GeneratorAdapter()
#         generator.set_filename("autogen_target.py")
#         generator.set_clazz(TankOperationsIMovable)
#         generator.set_target_dir(target_path)
#         generator.execute()
#         expected_file_path = os.path.join(
#             os.path.dirname(os.path.realpath(__file__)),
#             "test_data", "expected_autogen_target.py"
#         )
#         with open(expected_file_path) as expected_file_handler:
#             expected_content = expected_file_handler.read()
#
#         with open(os.path.join(ClassInfo.get_dir(TankOperationsIMovable),
#                                "autogen_target.py")) as target_file_handler:
#             actual_content = target_file_handler.read()
#         assert actual_content == expected_content
