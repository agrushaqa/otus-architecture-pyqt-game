import time

from features.steps.src.ioc.common import IoC
from features.steps.src.ioc_commands_queue import IocCommandQueue
from features.steps.src.ioc_working_thread import WorkingThread
from features.steps.src.scope import Scopes


def init_scope(scope, ioc, game_id):
    scope.new_clean_existing(game_id)
    scope.set_current(game_id)
    scope.current(ioc)


class TestGame:
    def test_game_one_thread(self):
        command_queue1 = IocCommandQueue()
        thread = WorkingThread(
            target=command_queue1.commands_worker,
            scope=Scopes(),
            ioc=IoC(),
            daemon=True)
        command_queue1.register_ioc_command("SoftStop",
                                            command_queue1.soft_stop)
        command_queue1.register_ioc_command("Sleep", time.sleep)
        command_queue1.register_ioc_command("ScopeCurrent", init_scope)

        thread.start()
        command_queue1.add_ioc_command("SoftStop")
        myscope = thread.get_scope()
        command_queue1.add_ioc_command("ScopeCurrent",
                                       myscope,
                                       thread.get_ioc(),
                                       "game1")
        thread.join()
        assert list(myscope._get('main').keys()) == ['IoC.register',
                                                     'SoftStop',
                                                     'Sleep',
                                                     'ScopeCurrent']
        assert list(myscope._get('game1').keys()) == ['IoC.register']

    def test_game_two_thread_soft_stop(self):
        command_queue1 = IocCommandQueue()
        command_queue2 = IocCommandQueue()
        thread1 = WorkingThread(
            target=command_queue1.commands_worker,
            scope=Scopes(),
            ioc=IoC(),
            daemon=True)
        thread2 = WorkingThread(
            target=command_queue2.commands_worker,
            scope=Scopes(),
            ioc=IoC(),
            daemon=True)
        command_queue1.register_ioc_command("SoftStop",
                                            command_queue1.soft_stop)
        command_queue2.register_ioc_command("SoftStop",
                                            command_queue2.soft_stop)
        thread1.start()
        thread2.start()
        scope_thread1 = thread1.get_scope()
        scope_thread2 = thread2.get_scope()
        command_queue1.add_ioc_command("SoftStop")
        command_queue2.add_ioc_command("SoftStop")
        thread1.join()
        thread2.join()
        assert list(scope_thread1._get('main').keys()) == ['IoC.register',
                                                           'SoftStop']
        assert list(scope_thread2._get('main').keys()) == ['IoC.register',
                                                           'SoftStop']

    def test_game_two_thread_hard_stop(self):
        command_queue1 = IocCommandQueue()
        command_queue2 = IocCommandQueue()
        thread1 = WorkingThread(
            target=command_queue1.commands_worker,
            scope=Scopes(),
            ioc=IoC(),
            daemon=True)
        thread2 = WorkingThread(
            target=command_queue2.commands_worker,
            scope=Scopes(),
            ioc=IoC(),
            daemon=True)
        command_queue1.register_ioc_command("HardStop",
                                            command_queue1.stop)
        command_queue2.register_ioc_command("HardStop",
                                            command_queue2.stop)
        thread1.start()
        thread2.start()
        scope_thread1 = thread1.get_scope()
        scope_thread2 = thread2.get_scope()
        command_queue1.add_ioc_command("HardStop")
        command_queue2.add_ioc_command("HardStop")
        thread1.join()
        thread2.join()
        assert list(scope_thread1._get('main').keys()) == ['IoC.register',
                                                           'HardStop']
        assert list(scope_thread2._get('main').keys()) == ['IoC.register',
                                                           'HardStop']
