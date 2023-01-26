from threading import Thread, local

thread_local = local()


class WorkingThread(Thread):
    def __init__(self, target, scope, ioc, group=None, name=None,
                 args=(), kwargs=None, daemon=None):
        super().__init__(target=target,
                         group=group,
                         name=name,
                         args=args,
                         kwargs=kwargs,
                         daemon=daemon)
        self.scope = scope
        self.ioc = ioc

    def run(self):
        self.get_scope().current(self.get_ioc())
        self._target(self.get_ioc(), *self._args, **self._kwargs)

    def get_scope(self):
        try:
            return self.scope
        except Exception:
            return None

    def get_ioc(self):
        try:
            return self.ioc
        except Exception:
            return None

    def get_thread_name(self):
        return self.name
